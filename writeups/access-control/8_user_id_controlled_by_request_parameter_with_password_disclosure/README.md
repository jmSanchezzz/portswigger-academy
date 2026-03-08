# User ID controlled by request parameter with password disclosure

## 1. Lab Information
**Title:** Lab: User ID controlled by request parameter with password disclosure  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Access Control (IDOR / Information Disclosure)

## 2. Lab Objective
Exploit an Insecure Direct Object Reference (IDOR) vulnerability to access the account page of another user. Because the application insecurely populates the password field with the user's actual password, the goal is to extract the administrator's password from the HTML source, log in to their account, and delete the user `carlos`.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and logged in using the provided credentials (`wiener:peter`). Navigated to the "My account" page and observed the `id` parameter in the URL. Switched to Burp Suite, located the `GET /my-account?id=wiener` request in the HTTP history, and sent it to Burp Repeater.
   
   <img width="1904" height="903" alt="image" src="https://github.com/user-attachments/assets/5ccaf4de-d1bc-43af-821c-e70bca637224" />

   *Figure 1 - Burp Suite HTTP history showing the GET request to the authenticated user's account page.*

2. In Burp Repeater, modified the `id` parameter in the URL from `wiener` to `administrator`.
   

   <img width="1322" height="327" alt="image" src="https://github.com/user-attachments/assets/52885dd7-10fd-466b-a47f-7f1421c19d9d" />

   *Figure 2 - Burp Repeater showing the modified GET request targeting the administrator's user ID.*

3. Clicked "Send". The server processed the IDOR payload and returned the HTML content for the administrator's account page. Scrolled through the response body and located the password input field, which contained the administrator's actual password in plaintext within the `value` attribute. Copied this password.
   
   <img width="1473" height="366" alt="image" src="https://github.com/user-attachments/assets/ca29aee0-2199-4210-9d32-9c69e7a9a413" />

   *Figure 3 - The server's response highlighting the administrator's password exposed in the HTML source code.*

4. Returned to the web browser, logged out of the `wiener` account, and navigated back to the login page. Authenticated using the username `administrator` and the extracted password.
   
   <img width="1916" height="741" alt="image" src="https://github.com/user-attachments/assets/4eb6dd31-2af7-4957-9832-a850c388724c" />

   *Figure 4 - Successfully logging into the application as the administrator.*

5. Accessed the newly available "Admin panel" from the navigation menu. Located the user `carlos` and clicked the "Delete" link. The server executed the action, successfully solving the lab.
   
   <img width="1899" height="620" alt="image" src="https://github.com/user-attachments/assets/2cff8497-c509-4def-9cce-17f3235cebfd" />

   *Figure 5 - The admin panel showing the successful deletion of user carlos and the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```http
?id=administrator
