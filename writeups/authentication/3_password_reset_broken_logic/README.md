# Password reset broken logic

## 1. Lab Information
**Title:** Lab: Password reset broken logic  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Authentication (Broken Logic / Flawed Password Reset)

## 2. Lab Objective
Exploit a logical flaw in the password reset functionality where the reset token is not strictly validated upon submission. The goal is to manipulate the POST request to reset the password for the target user `carlos`, log into his account, and access his "My account" page.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Proxy and Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and navigated to the login page. Clicked "Forgot your password?" and submitted a password reset request for the baseline user `wiener`.
   
   <img width="1901" height="610" alt="image" src="https://github.com/user-attachments/assets/66090437-ee5d-4ce3-a9dd-f02e103292d4" />

   *Figure 1 - Initiating a password reset request for the baseline account.*

2. Accessed the simulated Email client to retrieve the reset link. Clicked the link and completed the password reset process. Switched to Burp Suite, located the final `POST /forgot-password?temp-forgot-password-token=...` request in the HTTP history, and sent it to Burp Repeater.
   
   <img width="1903" height="949" alt="image" src="https://github.com/user-attachments/assets/c5c3d5e7-0c50-4328-b3f1-ed09b663d7e1" />

   *Figure 2 - Burp Suite HTTP history showing the POST request used to finalize the password reset.*

3. In Burp Repeater, analyzed the POST request. Noted that the request body insecurely contained a hidden `username` parameter alongside the new passwords and the token. Experimented by deleting the token value from both the URL query string and the request body (leaving them completely blank), and sent the request.
   
   <img width="1474" height="470" alt="image" src="https://github.com/user-attachments/assets/a0dd1b0f-fc40-4785-937d-d96615137e64" />

   *Figure 3 - Burp Repeater showing the modified request with the token values removed.*

4. Observed that the server responded with a successful status redirect, confirming that the backend does not actually validate the presence of the token when updating the password. It solely trusts the hidden `username` parameter to identify the account.
   
   <img width="1466" height="526" alt="image" src="https://github.com/user-attachments/assets/22e7ee57-bfd1-465f-af27-31cec9bbc718" />

   *Figure 4 - The server response confirming the password reset succeeded without a valid token.*

5. Generated a fresh password reset request in the browser. Intercepted the new `POST /forgot-password` request and sent it to Repeater. Deleted the token values once again. This time, modified the hidden `username` parameter in the request body from `wiener` to the victim `carlos`. Changed the password fields to a known value (e.g., `hacked123`).
   
   

   <img width="1319" height="325" alt="image" src="https://github.com/user-attachments/assets/a42b62d1-38ea-47fb-bceb-80ad1ca596a9" />

   *Figure 5 - Burp Repeater showing the final payload targeting Carlos's account with a blank token.*

6. Clicked "Send". The server successfully processed the request, resetting Carlos's password. Returned to the browser, navigated to the login page, and authenticated using the username `carlos` and the newly set password. The application granted access, successfully solving the lab.
   
   <img width="1903" height="780" alt="image" src="https://github.com/user-attachments/assets/b6300339-f367-491c-89c5-2b7067c52d10" />

   *Figure 6 - Successfully logging into Carlos's account, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
**Modified Request Body**
```http
temp-forgot-password-token=&username=carlos&new-password-1=hacked123&new-password-2=hacked123
```
*(Ensure the token is also removed from the URL endpoint: `POST /forgot-password?temp-forgot-password-token=`)*

## 6. Mitigation / Remediation
To prevent password reset logic flaws, applications must strictly validate tokens and never trust client-provided parameters for state management.
* **Strict Token Validation:** Password reset tokens must be tied securely to the specific user requesting the reset. During the final password update POST request, the backend must verify that the token is present, valid, unexpired, and matches the user attempting the reset.
* **Never Trust Client Data:** Do not rely on hidden form fields (like a `username` parameter) to determine whose password is being reset. The backend should exclusively use the cryptographically secure token to look up the associated user account in the database.
