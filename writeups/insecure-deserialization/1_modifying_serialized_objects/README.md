# Modifying serialized objects

## 1. Lab Information
**Title:** Lab: Modifying serialized objects  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Insecure Deserialization (Privilege Escalation)

## 2. Lab Objective
Exploit a serialization-based session mechanism to elevate privileges. The goal is to decode the session cookie, modify the serialized PHP object to grant administrative privileges, re-encode it, and then access the admin panel to delete the user `carlos`.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Proxy, Repeater, and Inspector)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and logged in using the provided credentials (`wiener:peter`). Navigated to the "My account" page. In Burp Suite's HTTP history, located the post-login `GET /my-account` request and observed the session cookie, which appeared to be URL-encoded and Base64-encoded. Sent this request to Burp Repeater.
   
   <img width="1873" height="896" alt="image" src="https://github.com/user-attachments/assets/c08d6367-4dbe-4b61-947a-9893fbdb5b39" />

   *Figure 1 - Burp Suite HTTP history showing the GET /my-account request and the encoded session cookie.*

2. In Burp Repeater, highlighted the session cookie value and used the Inspector panel on the right side to view the decoded payload. Identified that the decoded cookie was a serialized PHP object containing an `admin` attribute set to `b:0` (indicating the boolean value `false`).
   
   <img width="1880" height="399" alt="image" src="https://github.com/user-attachments/assets/017c6aeb-8da7-435f-9aba-ec494d414694" />

   *Figure 2 - Burp Suite Inspector panel revealing the decoded PHP serialized object and the admin attribute.*

3. Still using the Inspector panel, modified the value of the `admin` attribute from `b:0` to `b:1` (boolean `true`). Clicked "Apply changes" to automatically re-encode the payload and update the session cookie in the main request window.
   
   
   <img width="712" height="399" alt="image" src="https://github.com/user-attachments/assets/896d1e49-54f2-4552-90fb-6025570a54ad" />

   *Figure 3 - Modifying the admin boolean value to true using the Inspector panel.*

4. Clicked "Send" to issue the request with the forged session cookie. Examined the server's response and observed a link to the `/admin` panel, confirming the privilege escalation was successful.
   
   <img width="1181" height="762" alt="image" src="https://github.com/user-attachments/assets/4e99d920-aa4a-4468-bb4d-6dc26979281c" />

   *Figure 4 - The server response confirming administrative access by revealing the /admin link.*

5. Modified the HTTP request path to `GET /admin` and sent it to view the admin panel. Identified the endpoint for deleting users. Changed the request path once more to `GET /admin/delete?username=carlos` and clicked "Send". The server executed the action, successfully solving the lab.
   
   <img width="1173" height="490" alt="image" src="https://github.com/user-attachments/assets/a8cc2168-b636-4de4-8571-237ef3237771" />
   <img width="1903" height="240" alt="image" src="https://github.com/user-attachments/assets/aea6f609-4cac-4e97-b34f-19206e78930b" />


   *Figure 5 - Sending the final deletion payload to the admin endpoint, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
**Modified PHP Serialized Object (Decoded representation)**
```php
O:4:"User":2:{s:8:"username";s:6:"wiener";s:5:"admin";b:1;}
```

## 6. Mitigation / Remediation
To prevent insecure deserialization vulnerabilities, applications must avoid passing serialized objects containing sensitive state data to the client.
* **Server-Side Session Management:** Store session states and user privileges securely on the backend database or in a server-side session object. Issue a cryptographically secure, unpredictable, and opaque session ID to the client's cookie.
* **Digital Signatures:** If complex data structures absolutely must be serialized and sent to the client, the application must apply a robust digital signature (like an HMAC) to the serialized string. The server must verify this signature before attempting to deserialize the object to ensure it has not been tampered with.
