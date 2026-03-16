# Basic password reset poisoning

## 1. Lab Information
**Title:** Lab: Basic password reset poisoning  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Host Header Vulnerabilities / Business Logic

## 2. Lab Objective
Exploit a password reset poisoning vulnerability caused by the application dynamically generating password reset links based on the user-supplied HTTP Host header. The goal is to intercept the password reset request, inject the Exploit Server's domain into the Host header, steal the simulated victim Carlos's reset token from the access logs when he clicks the poisoned link, and use it to compromise his account.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Proxy - HTTP History and Repeater)
* Lab Exploit Server (Email Client and Access Logs)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and navigated to the "Forgot password" page. Submitted a password reset request for the provided attacker account (`wiener`). Navigated to the Exploit Server, opened the Email Client, and examined the legitimate password reset email to understand the URL structure and the `temp-forgot-password-token` parameter.
   
   <img width="1550" height="613" alt="image" src="https://github.com/user-attachments/assets/06beba12-847d-40d5-953d-f6f804a31bb5" />

   *Figure 1 - Reviewing the baseline password reset email and token structure in the Exploit Server Email Client.*

2. Switched to Burp Suite and navigated to **Proxy > HTTP history**. Located the `POST /forgot-password` request used to trigger the email. Right-clicked the request and selected "Send to Repeater".
   
   <img width="1493" height="383" alt="image" src="https://github.com/user-attachments/assets/98c05d02-166c-4e40-948f-74dda31a1702" />

   *Figure 2 - Sending the POST /forgot-password request to Burp Repeater.*

3. In Burp Repeater, modified the request to target the victim. Changed the `username` parameter in the request body to `carlos`. Additionally, modified the `Host` header at the top of the request, replacing the lab's legitimate domain with the Exploit Server's domain (e.g., `exploit-xxxx.exploit-server.net`). Clicked "Send".
   
   <img width="1491" height="670" alt="image" src="https://github.com/user-attachments/assets/1496d067-b33c-4dfb-b998-c5dbe0dfe822" />

   *Figure 3 - Burp Repeater showing the modified Host header and target username to execute the password reset poisoning.*

4. Returned to the Exploit Server and opened the **Access log**. Waited a moment for the simulated victim (Carlos) to receive the poisoned email and click the malicious link. Located the incoming `GET /forgot-password` request in the logs originating from Carlos, which contained his unique `temp-forgot-password-token` in the URL parameters. Copied this token.
   
   <img width="1897" height="904" alt="image" src="https://github.com/user-attachments/assets/2d6efa6f-ed87-4baa-955a-30d2325f827a" />

   *Figure 4 - The Exploit Server Access log revealing Carlos's stolen password reset token.*

5. In the web browser, constructed the final exploit URL by combining the lab's legitimate base domain, the `/forgot-password` path, and Carlos's stolen token: `https://[LAB-ID].web-security-academy.net/forgot-password?temp-forgot-password-token=[STOLEN-TOKEN]`. Navigated to this URL.
   
   <img width="1890" height="673" alt="image" src="https://github.com/user-attachments/assets/f0974b07-c5ac-459b-92ef-1b01e0e05d75" />

   *Figure 5 - Accessing the password reset form using Carlos's stolen token.*

6. The application accepted the token and presented the password reset form. Entered a new, known password for Carlos and submitted the form. Navigated to the main login page, logged in using the credentials `carlos` and the newly set password, and successfully solved the lab.
   
   <img width="1894" height="515" alt="image" src="https://github.com/user-attachments/assets/42816281-5af3-471c-81c1-7ed3638b1f85" />


   *Figure 6 - Successfully logging into Carlos's account, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
**Modified HTTP Request**
> `Host: [YOUR-EXPLOIT-SERVER-ID].exploit-server.net`
> `username=carlos`

## 6. Mitigation / Remediation
To prevent password reset poisoning and other Host header vulnerabilities, applications must not trust the user-supplied Host header when generating absolute URLs.
* **Use Relative URLs:** Whenever possible, applications should generate relative URLs instead of absolute URLs for links.
* **Define a Base URL Configuration:** If absolute URLs are strictly required (such as in password reset emails), the base domain should be hard-coded or strictly defined in a secure, server-side configuration file. The application must reference this trusted configuration variable rather than dynamically constructing the domain from the incoming HTTP Host header.
* **Validate the Host Header:** If the application must support multiple domains and use the Host header, strictly validate the incoming header against an explicitly defined whitelist of permitted, trusted domains.
