# Authentication bypass via OAuth implicit flow

## 1. Lab Information
**Title:** Lab: Authentication bypass via OAuth implicit flow  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** OAuth Authentication

## 2. Lab Objective
Exploit a flawed implementation of the OAuth implicit flow where the client application fails to securely validate the user associated with the provided access token. The goal is to intercept the final authentication request, modify the email parameter, and bypass the validation to log in as the victim, Carlos (`carlos@carlos-montoya.net`).

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Proxy - HTTP History and Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and clicked "My account" to initiate the OAuth login process. Logged in using the provided attacker social media credentials (`wiener:peter`), authorized the application, and completed the flow to return to the blog website.
   
   <img width="1899" height="493" alt="image" src="https://github.com/user-attachments/assets/f7d13a12-00a1-4c67-b77a-67a8757e2ffb" />

   *Figure 1 - Completing the legitimate OAuth login flow using the attacker's credentials.*

2. Switched to Burp Suite and navigated to **Proxy > HTTP history** to review the sequence of OAuth transactions. Identified the critical `POST /authenticate` request, where the client application sends the user's email, username, and OAuth token back to its own backend to establish the user session.
   
   <img width="1914" height="344" alt="image" src="https://github.com/user-attachments/assets/54400551-6161-48b9-821c-e4c96305713b" />

   *Figure 2 - Locating the POST /authenticate request in Burp HTTP history.*

3. Right-clicked the `POST /authenticate` request and selected "Send to Repeater" to test if the application strictly binds the access token to the specific email address provided by the OAuth service.
   
   <img width="1497" height="390" alt="image" src="https://github.com/user-attachments/assets/07771eb0-631b-46ed-b2cc-ab51a4a369e9" />

   *Figure 3 - Sending the authentication request to Burp Repeater for manipulation.*

4. In Burp Repeater, located the JSON body payload. Modified the `email` value, changing it from the attacker's email to the target victim's email (`carlos@carlos-montoya.net`). Clicked "Send" and observed a `200 OK` response that set a new session cookie, indicating the server blindly trusted the spoofed email address.
   
   <img width="1498" height="378" alt="image" src="https://github.com/user-attachments/assets/b1cc30ce-4b72-42f5-8601-6db9d04ff402" />

   *Figure 4 - Modifying the email parameter in the JSON payload to target Carlos's account.*

5. To easily apply this newly hijacked session to the web browser, right-clicked anywhere within the modified `POST` request in Burp Repeater and selected **Request in browser > In original session**. Copied the generated Burp Suite URL.
   
   <img width="1496" height="620" alt="image" src="https://github.com/user-attachments/assets/ffe751e1-0199-4130-b7c2-07307815e9f6" />

   *Figure 5 - Generating the "Request in browser" URL to hijack the session.*

6. Pasted the copied URL into the web browser's address bar and pressed Enter. The browser processed the request using the hijacked session cookie, successfully logging into Carlos's account and solving the lab.
   
   <img width="1898" height="250" alt="image" src="https://github.com/user-attachments/assets/ab5ba2bb-a8cd-4aec-b9f7-0d1faaa75a07" />

   *Figure 6 - Successfully accessing Carlos's account, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
**Modified JSON Payload**
> `{"email":"carlos@carlos-montoya.net","username":"carlos","token":"[OAUTH_TOKEN_REDACTED]"}`

## 6. Mitigation / Remediation
To prevent authentication bypasses in OAuth implementations, applications must never trust identity data submitted directly from the client's browser.
* **Verify Tokens Server-Side:** The client application's backend server must verify the access token directly with the OAuth provider (e.g., by sending the token to the provider's `/userinfo` endpoint). The backend should establish the user session based only on the identity claims returned securely by the provider, not by the client.
* **Do Not Trust Client-Submitted Identity:** Never rely on user IDs, email addresses, or usernames sent from the client-side application to an authentication endpoint. These values can be easily intercepted and modified by an attacker using an interception proxy.
* **Use the Authorization Code Flow:** The OAuth Implicit flow is largely deprecated due to its inherent security risks (like exposing tokens in the URL). Implement the more secure Authorization Code flow (with PKCE for public clients) instead.
