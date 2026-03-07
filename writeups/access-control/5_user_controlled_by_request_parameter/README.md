# User ID controlled by request parameter

## 1. Lab Information
**Title:** Lab: User ID controlled by request parameter  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Access Control (Horizontal Privilege Escalation / IDOR)

## 2. Lab Objective
Exploit an Insecure Direct Object Reference (IDOR) vulnerability on the user account page. The goal is to manipulate the `id` parameter in the URL to horizontally escalate privileges, access the account page of the user `carlos`, retrieve his API key, and submit it to solve the lab.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and logged in using the provided credentials (`wiener:peter`). Navigated to the "My account" page and observed that the URL contained a predictable user ID parameter (e.g., `/my-account?id=wiener`). Located this `GET` request in Burp Suite's HTTP history and sent it to Burp Repeater.
   
   <img width="1485" height="401" alt="image" src="https://github.com/user-attachments/assets/2bb3f464-e585-4e0b-87e5-b31fa489654c" />

   *Figure 1 - Burp Suite HTTP history showing the GET request to the account page with the predictable 'id' parameter.*

2. In Burp Repeater, analyzed the request and modified the `id` parameter in the URL path, changing it from `wiener` to the target user `carlos`.
   
   <img width="1471" height="404" alt="image" src="https://github.com/user-attachments/assets/59bb5240-73ee-43b9-ab15-0be6dc2bfa15" />

   *Figure 2 - Burp Repeater showing the modified GET request targeting the ID for user carlos.*

3. Clicked "Send". The server processed the request without properly verifying if the logged-in session belonged to the requested user ID. The server responded with a `200 OK` status and returned the HTML content for Carlos's account page.
   
   <img width="1473" height="633" alt="image" src="https://github.com/user-attachments/assets/d4266fde-8b76-48cb-b51d-df3439bdfa9b" />

   *Figure 3 - The server response returning the account details for Carlos.*

4. Scanned the returned HTML response body and located Carlos's private API key displayed within the page source. Copied this API key value.
   
   <img width="1476" height="499" alt="image" src="https://github.com/user-attachments/assets/eafc5b7e-652a-4689-8542-832205bb8be5" />

   *Figure 4 - Highlighting the exfiltrated API key belonging to carlos in the HTTP response.*

5. Returned to the lab environment in the web browser. Clicked the "Submit solution" button, pasted Carlos's API key into the input field, and submitted it to successfully solve the lab.
   
   <img width="1909" height="242" alt="image" src="https://github.com/user-attachments/assets/22d21c6f-fae4-49d4-90c4-013d90f6f051" />

   *Figure 5 - The "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```http
?id=carlos
