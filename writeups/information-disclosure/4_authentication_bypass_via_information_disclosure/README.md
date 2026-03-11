# Authentication bypass via information disclosure

## 1. Lab Information
**Title:** Lab: Authentication bypass via information disclosure  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Information Disclosure / Authentication Bypass

## 2. Lab Objective
Exploit an authentication bypass vulnerability by discovering a hidden custom HTTP header used by the front-end to verify local IP addresses. The goal is to use the HTTP TRACE method to leak the header name, configure Burp Suite to automatically inject this header to spoof a local connection (127.0.0.1), access the admin interface, and delete the user carlos.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Repeater, Proxy - Match and replace)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and sent a standard `GET /admin` request to Burp Repeater. Clicked "Send" and observed the response, which disclosed that the admin panel is only accessible if logged in as an administrator or if requested from a local IP address.
   
   <img width="1174" height="708" alt="image" src="https://github.com/user-attachments/assets/e64e500d-0220-4b1b-873c-29ba1e44bc03" />

   *Figure 1 - Burp Repeater showing the GET /admin request and the resulting access denial message.*

2. In Burp Repeater, changed the HTTP method from `GET` to `TRACE` and clicked "Send". Examined the server's response, which echoed the request back. Discovered that an internal proxy/load balancer was automatically appending a custom header (`X-Custom-IP-Authorization`) containing the external IP address.
   

   <img width="1173" height="757" alt="image" src="https://github.com/user-attachments/assets/01a7cc0a-a91f-4449-b31b-3bf67b561255" />

   *Figure 2 - Using the TRACE method to leak the internal X-Custom-IP-Authorization header.*

3. To exploit this trust relationship, navigated to Burp Suite's **Proxy** tab, clicked on **Proxy settings** (the gear icon), and scrolled down to the **Match and replace rules** section. Clicked "Add" to create a new rule.
   
   <img width="1110" height="737" alt="image" src="https://github.com/user-attachments/assets/bdc3c496-f506-44a1-9c02-343fccff7913" />

   *Figure 3 - Navigating to the Match and replace rules in Burp Suite Proxy settings.*

4. Configured the new rule with the Type set to "Request header". Left the "Match" field entirely blank (to append it to every request) and entered the spoofed header into the "Replace" field: `X-Custom-IP-Authorization: 127.0.0.1`. Clicked "OK" to enable the rule.
   
   <img width="1110" height="735" alt="image" src="https://github.com/user-attachments/assets/d5c5a266-842c-4747-8f30-e19277ae49d3" />

   *Figure 4 - Configuring the Match and replace rule to inject the spoofed localhost IP header.*

5. Returned to the web browser and navigated to the `/admin` endpoint. Because Burp Proxy automatically injected the spoofed header into the request, the backend system treated the connection as a trusted local request, bypassing the authentication check and granting access to the Admin panel.
   
   <img width="1890" height="627" alt="image" src="https://github.com/user-attachments/assets/76c27998-815f-45a1-9323-629d247bcbca" />

   *Figure 5 - Successfully accessing the Admin panel via the spoofed local IP header.*

6. Located the target user `carlos` in the admin interface and clicked the "Delete" button. The server processed the deletion, successfully solving the lab.
   
   <img width="1900" height="589" alt="image" src="https://github.com/user-attachments/assets/6e7278d4-6919-400b-9847-aa0646132b98" />

   *Figure 6 - Deleting the user carlos, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
**Spoofed Custom HTTP Header**
> `X-Custom-IP-Authorization: 127.0.0.1`

## 6. Mitigation / Remediation
To prevent authentication bypass and information disclosure via HTTP headers, applications must enforce strict method controls and validate the source of internal headers.
* **Disable the TRACE Method:** The HTTP `TRACE` method is designed for diagnostic purposes and echoes the received request back to the client. This can easily leak sensitive internal headers added by reverse proxies or load balancers. Disable the `TRACE` method entirely on production web servers.
* **Do Not Trust Client Headers for Authentication:** Never rely solely on HTTP headers (like `X-Forwarded-For` or custom IP headers) for access control or authentication, as they can be easily spoofed by an attacker.
* **Strip External Headers:** If the backend architecture relies on custom internal headers, the edge server (load balancer or reverse proxy) must strictly strip or overwrite any incoming headers from the external client that attempt to spoof these internal variable names.
