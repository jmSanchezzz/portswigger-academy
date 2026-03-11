# Information disclosure on debug page

## 1. Lab Information
**Title:** Lab: Information disclosure on debug page  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Information Disclosure

## 2. Lab Objective
Exploit a vulnerability where the application has left a sensitive debugging file accessible on the production server, the location of which is leaked via an HTML comment. The goal is to discover the debug page, extract the `SECRET_KEY` environment variable from its output, and submit it to solve the lab.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Proxy - HTTP History)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and browsed the home page. Switched to Burp Suite, navigated to **Proxy > HTTP history**, and located the initial `GET /` request for the home page.
   
   <img width="1911" height="912" alt="image" src="https://github.com/user-attachments/assets/e7e0ea24-39fb-4a8c-8585-49194521facf" />

   *Figure 1 - Burp Suite HTTP history showing the GET request for the home page.*

2. Selected the request and examined the corresponding HTTP response. Scrolled through the HTML source code and identified a suspicious HTML comment containing a link named "Debug". Noted that it pointed to the hidden path `/cgi-bin/phpinfo.php`.
   

   <img width="992" height="476" alt="image" src="https://github.com/user-attachments/assets/bac3020e-7bb1-423b-825e-4593e2b271bd" />

   *Figure 2 - Burp Suite Response tab highlighting the HTML comment with the hidden phpinfo path.*

3. Returned to the web browser and manually appended the discovered hidden path (`/cgi-bin/phpinfo.php`) to the lab's base URL in the address bar, then pressed Enter.
   
   <img width="1897" height="1031" alt="image" src="https://github.com/user-attachments/assets/df750bad-ca0f-4537-a6a9-e4448b320ced" />


   *Figure 3 - Accessing the /cgi-bin/phpinfo.php endpoint directly in the web browser.*

4. The server rendered the output of the `phpinfo()` function directly in the browser window. Scrolled through the verbose environment details and located the `SECRET_KEY` environment variable. Copied its value.
   
   <img width="1172" height="640" alt="image" src="https://github.com/user-attachments/assets/6bf812a5-af59-4835-baae-e818da38b532" />

   *Figure 4 - The phpinfo page in the browser revealing the SECRET_KEY environment variable.*

5. Navigated back to the main lab environment page. Clicked the "Submit solution" button, pasted the extracted `SECRET_KEY` into the input field, and submitted it to successfully solve the lab.
   
   <img width="565" height="287" alt="image" src="https://github.com/user-attachments/assets/3dfd025c-db9f-4bf2-ab75-480c28436d77" />
   <img width="1902" height="245" alt="image" src="https://github.com/user-attachments/assets/eca5acd0-cac8-4acc-95e0-c85809c89e04" />

   *Figure 5 - Submitting the exfiltrated environment variable, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
**URL Path Discovered**
```http
/cgi-bin/phpinfo.php
```

## 6. Mitigation / Remediation
To prevent this type of information disclosure, applications must strictly separate development/debugging environments from production.
* **Remove Debug Files:** Files utilized for testing and debugging (such as `phpinfo.php` in PHP environments) must be completely removed from the server before deploying to production.
* **Sanitize HTML Comments:** Ensure that HTML comments do not leak internal system architecture, sensitive file paths, or developer notes to the client side. Automated build processes should ideally strip out development comments before the HTML is served.
* **Restrict Access:** If diagnostic endpoints must exist in production for monitoring purposes, ensure they are strictly protected by robust authentication and authorization mechanisms, restricting access exclusively to authorized administrators.
