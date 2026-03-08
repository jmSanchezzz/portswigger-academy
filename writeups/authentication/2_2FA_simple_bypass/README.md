# 2FA simple bypass

## 1. Lab Information
**Title:** Lab: 2FA simple bypass  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Authentication (2FA Bypass)

## 2. Lab Objective
Exploit a flawed two-factor authentication (2FA) mechanism where the verification step does not enforce strict access controls on the application's internal pages. The goal is to authenticate using the victim's compromised credentials (`carlos:montoya`) and manually navigate past the 2FA prompt to access his account page.

## 3. Tools Used
* Web Browser

## 4. Step-by-Step Methodology

1. Accessed the lab environment and logged in using the provided baseline credentials (`wiener:peter`). Accessed the simulated email client, retrieved the 2FA verification code, and completed the login process. Navigated to the "My account" page and noted the endpoint URL (`/my-account`).
   
   <img width="1920" height="819" alt="image" src="https://github.com/user-attachments/assets/717398af-94f3-45fa-834b-705ce9ac4563" />

   *Figure 1 - Successfully logging into the baseline wiener account and identifying the /my-account endpoint.*

2. Logged out of the `wiener` account. Returned to the login page and authenticated using the victim's compromised credentials (`carlos:montoya`).
   
   <img width="1550" height="107" alt="image" src="https://github.com/user-attachments/assets/f6bba04b-5acc-4e4d-b980-0a4d8c9322c6" />

   *Figure 2 - Authenticating with the victim's credentials.*

3. The application redirected to the 2FA verification page, prompting for Carlos's 4-digit code. Instead of entering a code, manually clicked the browser's address bar and changed the URL to target the `/my-account` endpoint discovered in Step 1.
   
   

   <img width="1137" height="507" alt="image" src="https://github.com/user-attachments/assets/b782e5bc-7405-4df8-9aa2-02a89ec12172" />

   *Figure 3 - The 2FA verification prompt, showing the manual modification of the URL path in the browser's address bar.*

4. Pressed Enter. The application failed to verify whether the 2FA challenge had actually been completed for the current session. It loaded Carlos's account page directly, successfully solving the lab.
   
   <img width="1920" height="911" alt="image" src="https://github.com/user-attachments/assets/18c13046-2514-4829-a299-464c3fc73815" />

   *Figure 4 - Bypassing the 2FA prompt and accessing Carlos's account page, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```http
/my-account
```
## 6. Mitigation / Remediation
To prevent 2FA bypass vulnerabilities, applications must enforce strict session state handling throughout the entire authentication flow.
* **Strict State Enforcement:** The backend must track the user's authentication state (e.g., `Pre-Auth`, `2FA-Pending`, `Fully-Authenticated`).
* **Endpoint Protection:** Every single request to a restricted endpoint (like `/my-account`) must verify that the user's session is in the `Fully-Authenticated` state. If the session is still in the `2FA-Pending` state, the server should block the request and immediately redirect the user back to the 2FA verification page.
