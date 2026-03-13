# Host header authentication bypass

## 1. Lab Information
**Title:** Lab: Host header authentication bypass  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Host Header Vulnerabilities / Access Control

## 2. Lab Objective
Exploit a flawed access control mechanism that improperly relies on the HTTP Host header to verify local administrative privileges. The goal is to discover the hidden admin panel, spoof the Host header to simulate a local connection (`localhost`), access the interface, and delete the user `carlos`.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Proxy - HTTP History and Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment. To check for hidden directories, manually appended `/robots.txt` to the base URL in the web browser. Discovered a `Disallow` rule pointing to the `/admin` path.
   
   <img width="1111" height="162" alt="image" src="https://github.com/user-attachments/assets/6cbba507-2d42-4053-a02d-d6a408af434d" />

   *Figure 1 - Accessing the /robots.txt file and discovering the hidden /admin directory.*

2. Attempted to access the `/admin` panel directly in the web browser. The server rejected the request with a `401 Unauthorized` status code, but the error message explicitly leaked a critical piece of information: "Admin interface only available to local users."
   
   <img width="1113" height="399" alt="image" src="https://github.com/user-attachments/assets/b83582b5-68e0-423b-9376-cbdc1eeb6d18" />

   *Figure 2 - The access denied error message revealing that the admin panel requires a local connection.*

3. Switched to Burp Suite and navigated to **Proxy > HTTP history**. Located the failed `GET /admin` request. Right-clicked the request and selected "Send to Repeater".
   
   <img width="1502" height="552" alt="image" src="https://github.com/user-attachments/assets/e29822db-707f-48a8-818e-dada7a16adbf" />

   *Figure 3 - Sending the failed GET /admin request to Burp Repeater.*

4. In Burp Repeater, modified the `Host` header at the top of the request, replacing the lab's legitimate domain with `localhost` to spoof a local request. Clicked "Send". The server responded with a `200 OK` status, and the response body contained the HTML for the Admin panel.
   
   <img width="1490" height="710" alt="image" src="https://github.com/user-attachments/assets/aef43c73-32aa-4e8e-bf0b-fe6706e39eaa" />

   *Figure 4 - Burp Repeater showing the modified Host header (localhost) bypassing the authentication check and returning the admin panel.*

5. Reviewed the HTML response in Repeater to identify the action URL for deleting users. Modified the request line at the very top of the Repeater tab from `GET /admin HTTP/2` to `GET /admin/delete?username=carlos HTTP/2` (ensuring the `Host: localhost` header remained intact).
   <img width="1494" height="313" alt="image" src="https://github.com/user-attachments/assets/a74d2677-b8f0-437c-ab97-f7bd811a859b" />

   *Figure 5 - Modifying the request path in Burp Repeater to target the deletion endpoint for the user carlos.*

6. Clicked "Send" to execute the deletion request. The server processed the action and returned a `302 Found` redirect. Returned to the main lab environment in the web browser to successfully trigger the "Congratulations, you solved the lab!" banner.
   <img width="554" height="356" alt="image" src="https://github.com/user-attachments/assets/cf1b4165-c903-4bf3-8856-c23959dd1872" />
   <img width="1900" height="243" alt="image" src="https://github.com/user-attachments/assets/9dd0a79a-565f-4536-9191-b34141816d52" />

   *Figure 6 - The successful 302 redirect in Burp Repeater, followed by the lab completion banner.*

## 5. The Payload
**Spoofed Host Header & Target Path**
> `GET /admin/delete?username=carlos`
> `Host: localhost`

## 6. Mitigation / Remediation
To prevent Host header authentication bypasses, applications must implement robust access controls that do not rely on easily spoofed HTTP headers.
* **Do Not Trust the Host Header:** The HTTP `Host` header is entirely controlled by the client and can be easily manipulated. It must never be used as a primary mechanism to grant administrative privileges or verify the origin of a request.
* **Network-Level Access Control:** If an administrative interface is truly meant to be restricted to internal or local users, enforce this restriction at the network layer (e.g., using a firewall, VPC rules, or an API gateway) to block external IPs from reaching the `/admin` path entirely.
* **Strong Authentication:** Ensure all administrative interfaces require robust, session-based authentication (and ideally Multi-Factor Authentication), regardless of the network location or IP address the request supposedly originates from.
