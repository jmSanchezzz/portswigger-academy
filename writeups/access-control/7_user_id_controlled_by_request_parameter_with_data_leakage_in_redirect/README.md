# User ID controlled by request parameter with data leakage in redirect

## 1. Lab Information
**Title:** Lab: User ID controlled by request parameter with data leakage in redirect  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Access Control (IDOR / Data Leakage)

## 2. Lab Objective
Exploit an access control vulnerability where the application attempts to prevent unauthorized access by issuing a redirect, but inadvertently leaks sensitive information in the body of the redirect response. The goal is to manipulate the `id` parameter to target the user `carlos`, intercept the redirect response, extract his API key, and submit it to solve the lab.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and logged in using the provided credentials (`wiener:peter`). Navigated to the "My account" page. Switched to Burp Suite, located the `GET /my-account?id=wiener` request in the HTTP history, and sent it to Burp Repeater.
   
   <img width="1890" height="943" alt="image" src="https://github.com/user-attachments/assets/38bbfaa9-4d9b-47fd-8325-03b1884b51bf" />

   *Figure 1 - Burp Suite HTTP history showing the GET request to the user's own account page.*

2. In Burp Repeater, analyzed the request and modified the `id` parameter in the URL from `wiener` to `carlos`.
   

   <img width="1379" height="378" alt="image" src="https://github.com/user-attachments/assets/5b535f98-d021-4f6c-99d3-8de9d3869334" />

   *Figure 2 - Burp Repeater showing the modified GET request targeting Carlos's user ID.*

3. Clicked "Send". Observed that the server responded with an HTTP redirect status code (e.g., `302 Found` directing the user back to `/login` or the home page). However, scrolling down into the HTTP response body revealed that the application still rendered and leaked the entire HTML structure of Carlos's account page, including his private API key.
   
   <img width="1478" height="626" alt="image" src="https://github.com/user-attachments/assets/a5d9d93c-2c57-4fcf-a0b2-2f4f576d3537" />

   *Figure 3 - The server's redirect response, highlighting Carlos's leaked API key inside the response body.*

4. Copied the exfiltrated API key from the response body. Returned to the lab environment in the web browser, clicked the "Submit solution" button, and submitted the API key to successfully solve the lab.
   
   <img width="1908" height="510" alt="image" src="https://github.com/user-attachments/assets/49c26398-7330-4af0-8c38-192481e6d775" />
   <img width="1903" height="243" alt="image" src="https://github.com/user-attachments/assets/8b06b00a-2ad5-46ed-b913-f7d11f922a07" />

   *Figure 4 - Submitting the exfiltrated API key, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```http
?id=carlos
