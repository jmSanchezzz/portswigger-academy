# User ID controlled by request parameter, with unpredictable user IDs

## 1. Lab Information
**Title:** Lab: User ID controlled by request parameter, with unpredictable user IDs  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Access Control (Horizontal Privilege Escalation / IDOR)

## 2. Lab Objective
Exploit an Insecure Direct Object Reference (IDOR) vulnerability on the user account page. The application identifies users with unpredictable GUIDs instead of sequential IDs. The goal is to find the target user's (`carlos`) GUID via information disclosure, use it to horizontally escalate privileges, retrieve his API key, and submit it to solve the lab.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment's home page and located a blog post authored by the target user, `carlos`. Clicked on the author's name to view their profile. Observed the URL structure and copied the revealed user ID (a long, unpredictable GUID) assigned to `carlos` (e.g., `/blogs?userId=...`).
   
   <img width="1899" height="1026" alt="image" src="https://github.com/user-attachments/assets/1c0639e9-17ee-4829-bb65-acfd4b527cc7" />

   *Figure 1 - The browser displaying Carlos's author page, revealing his assigned GUID in the URL parameter.*

2. Navigated to the login page and authenticated using the provided credentials (`wiener:peter`). Accessed the "My account" page and located the `GET /my-account?id=...` request in Burp Suite's HTTP history. Sent this request to Burp Repeater.
   
   <img width="1905" height="1022" alt="image" src="https://github.com/user-attachments/assets/60f7b983-fe1e-4fb5-98d8-d7d1922047ad" />

   *Figure 2 - Burp Suite HTTP history showing the GET request to the account page using the authenticated user's own GUID.*

3. In Burp Repeater, modified the `id` parameter in the URL. Replaced `wiener`'s GUID with the exfiltrated GUID belonging to `carlos`.
   
   
   <img width="1468" height="379" alt="image" src="https://github.com/user-attachments/assets/09ce17f2-118d-4bfb-a178-fb49f3e0cd60" />

   *Figure 3 - Burp Repeater showing the modified GET request targeting Carlos's specific GUID.*

4. Clicked "Send". The server processed the request without validating if the currently logged-in session had authorization to view that specific GUID's profile. The server responded with a `200 OK` status, returning the HTML content for Carlos's account page. Scanned the response and copied Carlos's private API key.
   
   <img width="1472" height="376" alt="image" src="https://github.com/user-attachments/assets/2e9d2b59-bd17-4ca0-887e-977d407414fb" />

   *Figure 4 - Highlighting the exfiltrated API key belonging to carlos in the HTTP response.*

5. Returned to the lab environment in the web browser. Clicked the "Submit solution" button, pasted Carlos's API key into the input field, and submitted it to successfully solve the lab.
   
<img width="564" height="281" alt="image" src="https://github.com/user-attachments/assets/70806eac-bfd3-4d90-9a66-5db41b5a5844" />
<img width="1904" height="243" alt="image" src="https://github.com/user-attachments/assets/f70f1f79-14dd-4827-932a-2e1e909c010f" />


   *Figure 5 - Submitting the exfiltrated API key, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```http
?id=[CARLOS_GUID]
