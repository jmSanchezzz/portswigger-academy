# JWT authentication bypass via unverified signature

## 1. Lab Information
**Title:** Lab: JWT authentication bypass via unverified signature  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** JWT Vulnerabilities / Authentication Bypass

## 2. Lab Objective
Exploit a flawed JWT implementation where the backend server fails to verify the cryptographic signature of incoming tokens. The goal is to decode the JWT session cookie, modify the `sub` (subject) claim to impersonate the `administrator` user, access the restricted `/admin` panel, and delete the user `carlos`.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Proxy - HTTP History, Repeater, and Inspector)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and logged in using the provided standard credentials (`wiener:peter`).
   
   <img width="1033" height="436" alt="Image" src="https://github.com/user-attachments/assets/c34bc2a7-0325-42a6-9af2-bb67c33d9ba7" />

   *Figure 1 - Logging into the application using the standard user credentials.*

2. Switched to Burp Suite and navigated to **Proxy > HTTP history**. Located the post-login `GET /my-account` request. Observed that the application uses a JSON Web Token (JWT) as the session cookie. Right-clicked this request and selected "Send to Repeater".
   
   <img width="752" height="549" alt="Image" src="https://github.com/user-attachments/assets/9d147bff-80b1-4ddb-8d5b-4dca549c6961" />

   *Figure 2 - Identifying the JWT session cookie in the GET /my-account request.*

3. In Burp Repeater, changed the request path at the top from `GET /my-account` to `GET /admin` and clicked "Send". The server responded with a `401 Unauthorized` message, confirming that the admin panel is restricted.
   
   <img width="1493" height="714" alt="Image" src="https://github.com/user-attachments/assets/b34e3ef8-8b2d-43da-8512-92184ace9b1c" />

   *Figure 3 - Attempting to access the /admin panel and receiving an unauthorized response.*

4. In the request panel of Burp Repeater, highlighted the payload section of the JWT (the middle string of characters between the two periods). Looked at the Inspector panel on the right side of the screen to view the decoded JSON. Modified the `sub` claim value from `wiener` to `administrator` and clicked "Apply changes" to update the token in the request.
   
   <img width="378" height="169" alt="Image" src="https://github.com/user-attachments/assets/735a387b-dd7c-4a33-943b-b69a31df2cf0" />

   *Figure 4 - Using Burp Inspector to modify the JWT payload claim from wiener to administrator.*

5. Clicked "Send" with the modified JWT. The server responded with a `200 OK`, revealing the HTML for the admin panel. This confirmed that the server blindly trusted the modified payload without verifying the token's cryptographic signature.
   
   <img width="1501" height="752" alt="Image" src="https://github.com/user-attachments/assets/bd7fe206-8031-4270-bd88-752fcb606bc4" />

   *Figure 5 - Successfully bypassing authentication and accessing the admin interface using the forged JWT.*

6. Reviewed the HTML response to locate the user deletion endpoint. Modified the request path at the top of Repeater to `GET /admin/delete?username=carlos` (leaving the forged JWT cookie intact) and clicked "Send". The server processed the deletion, successfully solving the lab.
   
   <img width="1488" height="567" alt="Image" src="https://github.com/user-attachments/assets/3518a78d-6341-4679-91d8-701074ac1f80" />
   <img width="1898" height="239" alt="Image" src="https://github.com/user-attachments/assets/fa50bc24-0775-4cd6-89f0-7ab6b0c0f0b7" />

   *Figure 6 - Deleting the target user via the forged JWT, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
**Modified JWT Payload Claim**
> `"sub": "administrator"`

## 6. Mitigation / Remediation
To prevent JWT authentication bypasses, applications must strictly enforce cryptographic validation on every token received.
* **Enforce Signature Verification:** The backend server must be configured to verify the cryptographic signature of every incoming JWT before trusting any data or claims contained within its payload. If the signature is invalid or missing, the token must be immediately rejected.
* **Use Established Libraries:** Never attempt to write custom JWT parsing or verification logic. Utilize well-vetted, established, and up-to-date JWT libraries specific to your framework, and ensure they are explicitly configured to require strict signature validation.
* **Protect the Secret Key:** Ensure the secret key used by the server to sign and verify tokens is long, highly complex, and stored securely as an environment variable or in a dedicated secrets manager, never hard-coded in the application source code.
