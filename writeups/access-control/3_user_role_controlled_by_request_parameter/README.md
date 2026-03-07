# User role controlled by request parameter

## 1. Lab Information
**Title:** Lab: User role controlled by request parameter  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Access Control (Broken Access Control)

## 2. Lab Objective
Exploit a broken access control vulnerability where the application determines the user's privilege level using a forgeable client-side cookie. The goal is to elevate privileges to an administrator and access the `/admin` panel to delete the user `carlos`.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Proxy and Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and attempted to browse directly to the `/admin` path. The application denied access, confirming that administrative privileges are required.
   
   <img width="1919" height="1021" alt="image" src="https://github.com/user-attachments/assets/5c0acb61-086b-4188-a2a1-9e3a4dc54278" />

   *Figure 1 - The browser displaying an access denied or "Admin interface only available if logged in as an administrator" message.*

2. Navigated to the login page and authenticated using the provided credentials (`wiener:peter`). Switched to Burp Suite and reviewed the HTTP history for the `POST /login` request.
   
   <img width="1892" height="910" alt="image" src="https://github.com/user-attachments/assets/549668b2-5aed-47b5-8a92-c580ba600b18" />


   *Figure 2 - Burp Suite HTTP history showing the successful POST /login request.*

3. Examined the server's HTTP response to the login request. Observed that the server explicitly sets a cookie named `Admin` with the value `false` (`Set-Cookie: Admin=false`).
   
   <img width="1494" height="759" alt="image" src="https://github.com/user-attachments/assets/6c52550e-30d8-4c0b-84f0-bb3349f209ec" />

   *Figure 3 - The server's response setting the Admin=false cookie.*

4. Sent a `GET /admin` request to Burp Repeater. In the request headers, manually modified the `Admin` cookie value from `false` to `true`.
   
   

   <img width="1494" height="710" alt="image" src="https://github.com/user-attachments/assets/518192b6-f7d1-433c-b867-d2abb2df5803" />

   *Figure 4 - Burp Repeater showing the modified Cookie header (Admin=true) and the server responding with the HTML of the admin panel.*

5. Analyzed the returned HTML in the response panel to find the deletion endpoint for the user `carlos` (e.g., `/admin/delete?username=carlos`). Sent a final request to this endpoint, ensuring the `Admin=true` cookie was still included in the header. Clicked "Send". The server executed the action, successfully deleting the user and solving the lab.
   
   <img width="1496" height="701" alt="image" src="https://github.com/user-attachments/assets/dad905fd-7ddb-4e8b-8232-444c4eaa4e93" />
   <img width="1902" height="251" alt="image" src="https://github.com/user-attachments/assets/9d529f6c-7388-4232-aaad-6a71320cbb94" />

   *Figure 5 - The HTTP request delivering the deletion payload with the forged cookie, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```http
Cookie: Admin=true
