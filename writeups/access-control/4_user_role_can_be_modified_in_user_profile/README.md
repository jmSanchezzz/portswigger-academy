# User role can be modified in user profile

## 1. Lab Information
**Title:** Lab: User role can be modified in user profile  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Access Control (Mass Assignment / Broken Access Control)

## 2. Lab Objective
Exploit a mass assignment vulnerability in the user profile update feature. The goal is to append a restricted parameter (`roleid`) to the JSON request body to elevate privileges to administrator (role ID `2`), then access the `/admin` panel to delete the user `carlos`.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Proxy and Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and logged in using the provided credentials (`wiener:peter`). Navigated to the account page, used the feature to update the email address, and intercepted the resulting request in Burp Suite.
   
   <img width="1474" height="740" alt="image" src="https://github.com/user-attachments/assets/a1cfd852-3351-4b39-915e-2a34b0142bc8" />

   *Figure 1 - Burp Suite HTTP history showing the POST request used to update the user's email address.*

2. Reviewed the server's HTTP response to the email update. Observed that the JSON response explicitly returns the user's current role ID (e.g., `"roleid":1`), indicating the exact parameter name used by the backend.
   
   
   <img width="1470" height="444" alt="image" src="https://github.com/user-attachments/assets/69699c8c-0c14-40bd-bbe8-3c74912eab51" />

   *Figure 2 - The server's response reflecting the user's current roleid.*

3. Sent the email update request to Burp Repeater. Modified the JSON request body to inject the restricted parameter, adding `"roleid":2` alongside the email address.
   
   <img width="1476" height="442" alt="image" src="https://github.com/user-attachments/assets/f9e5a443-035c-44d6-b5b3-51e71bc9a3b9" />

   *Figure 3 - Burp Repeater showing the modified JSON body including the injected roleid parameter.*

4. Clicked "Send". Observed the server's response, which confirmed that the backend blindly accepted the input and successfully updated the user's `roleid` to `2`.
   <img width="1061" height="359" alt="image" src="https://github.com/user-attachments/assets/35354668-c67f-470d-b8fd-019fb37ab5ab" />

   *Figure 4 - The server response confirming the roleid has been changed to 2.*

5. Returned to the web browser and navigated to the `/admin` path. The application granted access based on the newly elevated privileges. Located the user `carlos` and clicked "Delete" to solve the lab.
   
   <img width="1916" height="644" alt="image" src="https://github.com/user-attachments/assets/c210f37f-b712-48cb-804b-39630a7066fb" />

   *Figure 5 - The admin panel showing the successful deletion of user carlos and the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```json
"roleid":2
