# File path traversal, simple case

## 1. Lab Information
**Title:** Lab: File path traversal, simple case  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Directory Traversal (File Path Traversal)

## 2. Lab Objective
Exploit a path traversal vulnerability in the application's product image display feature. The goal is to manipulate the `filename` parameter to step outside the designated image directory and retrieve the contents of the server's `/etc/passwd` file.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and navigated to a product page. Switched to Burp Suite and located a request that fetches a product image (e.g., `GET /image?filename=...`) in the HTTP history. Sent this request to Burp Repeater.
   
   <img width="1914" height="923" alt="image" src="https://github.com/user-attachments/assets/15769646-6c7c-4aff-9ac6-3c01670a2531" />

   *Figure 1 - Burp Suite HTTP history showing the GET request for a product image being sent to Repeater.*

2. In Burp Repeater, analyzed the request and identified the `filename` parameter used to load the image file from the server's backend.
   
   <img width="1491" height="320" alt="image" src="https://github.com/user-attachments/assets/8b075f66-ab4a-4ad4-bf97-05f1a8a9313e" />

   *Figure 2 - Burp Repeater showing the original image request with a standard filename.*

3. Modified the `filename` parameter to inject a path traversal payload. Replaced the legitimate image name with the sequence `../../../etc/passwd` to traverse up three levels in the directory tree and access the target system file.
   
   

   <img width="1491" height="377" alt="image" src="https://github.com/user-attachments/assets/4e5b2969-aeca-4802-8335-9a0bfe307c11" />

   *Figure 3 - Burp Repeater showing the modified filename parameter with the path traversal payload.*

4. Clicked "Send". The server processed the payload, escaped the intended image folder, and returned the contents of the `/etc/passwd` file directly in the HTTP response body, successfully solving the lab.
   
   <img width="1496" height="567" alt="image" src="https://github.com/user-attachments/assets/6252b67d-6af3-41af-832c-5ee4899762b4" />
   <img width="1900" height="252" alt="image" src="https://github.com/user-attachments/assets/5edeebdb-0514-4294-b456-d9e0f9a0a5c0" />

   *Figure 4 - The HTTP response displaying the exfiltrated contents of the /etc/passwd file, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```http
filename=../../../etc/passwd
