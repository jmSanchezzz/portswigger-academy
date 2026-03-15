# JWT authentication bypass via flawed signature verification

## 1. Lab Information
**Title:** Lab: JWT authentication bypass via flawed signature verification  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** JWT Vulnerabilities / Authentication Bypass

## 2. Lab Objective
Exploit a flawed JWT implementation that insecurely accepts tokens signed with the "none" algorithm. The goal is to capture the session JWT, modify the `alg` header to `none`, modify the `sub` claim to impersonate the `administrator` user, strip the cryptographic signature from the token, and use this forged session to delete the user `carlos`.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Proxy - HTTP History, Repeater, and Inspector)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and logged in using the provided standard credentials (`wiener:peter`).
   
   <img width="1009" height="428" alt="Image" src="https://github.com/user-attachments/assets/740cb5ad-8bc5-4dae-9927-bfdb32f5222e" />

   *Figure 1 - Logging into the application using the standard user credentials.*

2. Switched to Burp Suite and navigated to **Proxy > HTTP history**. Located the post-login `GET /my-account` request. Observed the JSON Web Token (JWT) being used as the session cookie. Right-clicked this request and selected "Send to Repeater".
   
   <img width="1920" height="900" alt="Image" src="https://github.com/user-attachments/assets/4e63838b-c2a7-4b91-b599-494002480855" />

   *Figure 2 - Identifying the JWT session cookie in the HTTP history.*

3. In Burp Repeater, changed the request path from `GET /my-account` to `GET /admin` and clicked "Send" to establish a baseline. The server returned a `401 Unauthorized` response, confirming that the admin panel requires administrative privileges.
   
   <img width="1496" height="717" alt="Image" src="https://github.com/user-attachments/assets/ffc4763f-f909-41a3-84a1-29001b8ba401" />

   *Figure 3 - Verifying the access restriction on the /admin panel using the standard user token.*

4. In the request panel, placed the cursor inside the JWT string. Used the Inspector panel on the right side of the screen to view the decoded JSON Web Token. Expanded the Payload section, modified the `sub` claim value from `wiener` to `administrator`, and clicked "Apply changes".
   
   <img width="388" height="173" alt="Image" src="https://github.com/user-attachments/assets/ca50c462-aaa3-4057-a6d5-6d4a9d7d7572" />

   *Figure 4 - Modifying the JWT payload sub claim to target the administrator account.*

5. Still in the Inspector panel, expanded the Header section of the JWT. Modified the `alg` (algorithm) parameter, changing its value to `none`, and clicked "Apply changes".
   
   <img width="401" height="185" alt="Image" src="https://github.com/user-attachments/assets/3a305cb1-758c-4c9b-b4b1-5b37562495f7" />

   *Figure 5 - Modifying the JWT header to exploit the "none" algorithm vulnerability.*

6. Returned to the raw request editor in Repeater. Located the newly modified JWT session cookie. Manually deleted the cryptographic signature string at the very end of the token, taking extreme care to leave the final trailing period (`.`) intact. Clicked "Send". The server accepted the unsigned token and returned a `200 OK` with the admin panel HTML.
   
   <img width="1493" height="708" alt="Image" src="https://github.com/user-attachments/assets/02856cf3-6a82-4a6a-9e6b-edf03c17b546" />

   *Figure 6 - Removing the JWT signature while retaining the trailing period, successfully bypassing authentication.*

7. Reviewed the HTML response to find the user deletion endpoint. Modified the request path at the top of Repeater to `GET /admin/delete?username=carlos` (leaving the forged, unsigned JWT cookie intact) and clicked "Send". The server executed the action, successfully solving the lab.
   
   <img width="1492" height="462" alt="Image" src="https://github.com/user-attachments/assets/524f59fc-da97-44b4-92b5-cf240d1a8ecb" />
   <img width="1902" height="247" alt="Image" src="https://github.com/user-attachments/assets/6af4a6dc-8675-4200-a3ff-06718b6372ae" />

   *Figure 7 - Executing the user deletion via the forged JWT, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
**Modified JWT Header & Payload (None Algorithm Bypass)**
> `"alg": "none"`
> `"sub": "administrator"`

## 6. Mitigation / Remediation
To prevent "none" algorithm bypass attacks, applications must strictly dictate and verify the cryptographic algorithms used for JWTs.
* **Reject the "None" Algorithm:** The backend server and its JWT library must be explicitly configured to reject any incoming token that specifies `none` as its signing algorithm.
* **Enforce Specific Algorithms:** Do not rely on the `alg` header provided by the client to determine how a token should be verified. The server should be hard-coded to expect and verify a specific algorithm (e.g., `RS256` or `HS256`) and immediately reject tokens that attempt to use anything else.
* **Keep Libraries Updated:** Use modern, well-maintained JWT libraries. Most modern libraries have been updated to reject the "none" algorithm by default due to how widespread this vulnerability became, but legacy systems may still require explicit configuration.
