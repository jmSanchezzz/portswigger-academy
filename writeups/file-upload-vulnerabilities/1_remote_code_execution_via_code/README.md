# Remote code execution via web shell upload

## 1. Lab Information
**Title:** Lab: Remote code execution via web shell upload  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** File Upload Vulnerabilities / Remote Code Execution (RCE)

## 2. Lab Objective
Exploit an unrestricted file upload function that fails to validate user-supplied files. The goal is to upload a basic PHP web shell, locate where the uploaded files are stored on the server's filesystem, execute the script to exfiltrate the contents of `/home/carlos/secret`, and submit the secret to solve the lab.

## 3. Tools Used
* Web Browser
* Text Editor (to create the payload)
* Burp Suite Community Edition (Proxy - HTTP History and Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and logged in using the provided credentials (`wiener:peter`). Navigated to the "My account" page and observed the avatar upload functionality. Uploaded a standard image file to establish a baseline of normal application behavior.
   
   <img width="923" height="173" alt="image" src="https://github.com/user-attachments/assets/9aea57f4-257a-4dd8-b34c-cb6bbed8cde6" />

   *Figure 1 - Uploading a standard image file to the avatar upload function.*

2. Switched to Burp Suite and navigated to **Proxy > HTTP history**. Located the `GET` request used by the application to fetch the newly uploaded avatar (e.g., `GET /files/avatars/<YOUR-IMAGE>`). Right-clicked this request and selected "Send to Repeater".
   
   <img width="1918" height="228" alt="image" src="https://github.com/user-attachments/assets/52be0a74-b8ee-4f16-8a91-40897e52a12a" />

   *Figure 2 - Identifying the storage directory for uploaded files in Burp HTTP history.*

3. On the local machine, opened a text editor and created a malicious PHP file named `exploit.php`. Inserted a basic PHP script designed to read and output the contents of the target secret file.
   
   <img width="704" height="179" alt="image" src="https://github.com/user-attachments/assets/2e2a0713-a10a-4831-8146-61230a6da70d" />

   *Figure 3 - Creating the exploit.php web shell payload.*

4. Returned to the web browser and used the avatar upload function to upload the `exploit.php` file. The application accepted the file without any validation errors and returned a success message.
   
   <img width="1037" height="183" alt="image" src="https://github.com/user-attachments/assets/c9cf3339-4d0e-4431-a748-26176125b8db" />

   *Figure 4 - The application successfully accepting and storing the PHP web shell.*

5. Switched to Burp Repeater. Modified the path of the previously captured `GET` request to point to the newly uploaded malicious file (`GET /files/avatars/exploit.php HTTP/1.1`).
   
   <img width="1492" height="707" alt="image" src="https://github.com/user-attachments/assets/2530da84-d9e3-49c2-bf8e-f8dafff4323d" />

   *Figure 5 - Executing the web shell via Burp Repeater and capturing Carlos's secret in the HTTP response.*

6. The server executed the PHP script instead of rendering it as an image, and returned Carlos's secret in the response body. Copied the exfiltrated secret, navigated back to the main lab interface, clicked "Submit solution", and submitted the secret to solve the lab.
   
   <img width="1898" height="237" alt="image" src="https://github.com/user-attachments/assets/d185b596-fd9d-4ef6-8b64-306371ce9778" />


   *Figure 6 - Submitting the exfiltrated secret, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
**Malicious PHP Web Shell (`exploit.php`)**
> `<?php echo file_get_contents('/home/carlos/secret'); ?>`

## 6. Mitigation / Remediation
To prevent remote code execution via file uploads, applications must strictly validate and isolate all user-supplied files.
* **Strict Extension Validation:** Implement a strict whitelist of allowed file extensions (e.g., `.jpg`, `.png`). Never rely on blacklists, as attackers can easily bypass them using alternate extensions (like `.php5` or `.phtml`).
* **Content-Type and Magic Byte Verification:** Do not rely solely on the `Content-Type` header from the client. Verify the actual contents of the file by checking its "magic bytes" (file signature) to ensure it matches the expected file type.
* **Disable Execution in Upload Directories:** Configure the web server (e.g., via `.htaccess` in Apache or location blocks in Nginx) to strictly prevent the execution of server-side scripts (like PHP, ASP, or JSP) within the directory where uploaded files are stored.
* **Rename Uploaded Files:** Automatically rename uploaded files to a randomly generated string (e.g., a UUID) to prevent attackers from easily guessing or addressing the location of their uploaded payloads.
