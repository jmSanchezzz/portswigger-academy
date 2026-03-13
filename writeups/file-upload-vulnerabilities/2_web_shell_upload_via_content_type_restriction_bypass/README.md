## 1. Lab Information
**Title:** Lab: Web shell upload via Content-Type restriction bypass  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** File Upload Vulnerabilities / Remote Code Execution (RCE)

## 2. Lab Objective
Exploit a file upload vulnerability where the server attempts to restrict file types but insecurely relies on the user-controllable HTTP `Content-Type` header for validation. The goal is to intercept the upload request, spoof the MIME type to bypass the filter, upload a PHP web shell, execute it to exfiltrate the contents of `/home/carlos/secret`, and submit the secret.

## 3. Tools Used
* Web Browser
* Text Editor (to create the payload)
* Burp Suite Community Edition (Proxy - HTTP History and Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and logged in using the provided credentials (`wiener:peter`). Navigated to the "My account" page, uploaded a standard image file as an avatar, and observed the normal application behavior.
   
   <img width="973" height="267" alt="image" src="https://github.com/user-attachments/assets/e52c7de4-e1af-48e3-a97c-3ce853e6c45b" />

   *Figure 1 - Uploading a standard image file to establish a baseline for the avatar upload function.*

2. On the local machine, created a malicious PHP file named `exploit.php` containing a script designed to read the target secret file. Attempted to upload `exploit.php` directly via the web interface and received an error stating that only `image/jpeg` or `image/png` MIME types are allowed.
   
   <img width="1205" height="242" alt="image" src="https://github.com/user-attachments/assets/2959c6f6-ac44-4e10-b3d3-8e3743e30f9f" />

   *Figure 2 - The application rejecting the PHP file upload based on its MIME type.*

3. Switched to Burp Suite and navigated to **Proxy > HTTP history**. Located the rejected `POST /my-account/avatar` request used to submit the PHP file. Right-clicked the request and selected "Send to Repeater". Additionally, located the `GET /files/avatars/<YOUR-IMAGE>` request from the earlier successful upload and sent it to Repeater as well.
   
   <img width="1490" height="503" alt="image" src="https://github.com/user-attachments/assets/178d8255-56dd-4c49-8651-2a090c312e68" />
   <img width="1499" height="493" alt="image" src="https://github.com/user-attachments/assets/c8cf6a1b-fdaf-4a0f-8485-770c006b2321" />

   *Figure 3 - Sending the blocked POST upload request and the GET fetch request to Burp Repeater.*

4. In Burp Repeater, viewed the `POST /my-account/avatar` request. Located the `Content-Type` header specifically within the `multipart/form-data` boundary corresponding to the uploaded file (which defaulted to `application/octet-stream`). Modified this value to `Content-Type: image/jpeg` and clicked "Send". The server accepted the spoofed MIME type and successfully uploaded the script.
   
   <img width="1489" height="700" alt="image" src="https://github.com/user-attachments/assets/a80f4705-ccdf-44a4-9c43-0d38c6b9c0af" />

   *Figure 4 - Bypassing the restriction by modifying the file's Content-Type header in Burp Repeater.*

5. Switched to the Repeater tab containing the `GET` request. Modified the path to point to the newly uploaded script: `GET /files/avatars/exploit.php HTTP/1.1`. Clicked "Send". The server executed the PHP code and returned Carlos's secret in the response.
   
   <img width="1493" height="665" alt="image" src="https://github.com/user-attachments/assets/2136c561-4d59-48e8-bc0a-f81c5b966b0c" />

   *Figure 5 - Executing the web shell via the modified GET request and capturing the exfiltrated secret.*

6. Copied the exfiltrated secret, navigated back to the main lab interface in the web browser, clicked "Submit solution", and pasted the secret to successfully solve the lab.
   
   <img width="569" height="285" alt="image" src="https://github.com/user-attachments/assets/42c5ea4c-9232-4a90-abf9-dedb25be6ce9" />
   <img width="1902" height="242" alt="image" src="https://github.com/user-attachments/assets/dc9e3643-13a7-473e-a0b6-0fd490559f66" />

   *Figure 6 - Submitting Carlos's secret, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
**Modified Content-Type Header & Web Shell (`exploit.php`)**
> `Content-Type: image/jpeg`
> `<?php echo file_get_contents('/home/carlos/secret'); ?>`

## 6. Mitigation / Remediation
To prevent file upload restriction bypasses, applications must implement robust, server-side validation that does not rely on user-controllable HTTP headers.
* **Do Not Trust the Content-Type Header:** The `Content-Type` header is supplied by the client and can easily be intercepted and modified by an attacker using a proxy. Never use it as the sole mechanism for validating file types.
* **Inspect File Contents (Magic Bytes):** The server should explicitly verify the file type by inspecting the actual contents of the uploaded file. This is typically done by reading the file's "magic bytes" (file signature) to ensure it genuinely matches the expected format (e.g., verifying a file starts with the hexadecimal signature for a JPEG).
* **Isolate and Disable Execution:** Store uploaded files in a dedicated, isolated directory outside the web root if possible. Configure the web server to strictly forbid the execution of server-side scripts (PHP, ASP, JSP, etc.) within the upload directory.
