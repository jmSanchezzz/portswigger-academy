# Unprotected admin functionality with unpredictable URL

## 1. Lab Information
**Title:** Lab: Unprotected admin functionality with unpredictable URL  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Access Control (Broken Access Control)

## 2. Lab Objective
Exploit a broken access control vulnerability where an administrative panel is unprotected but hosted at an unpredictable, obscure URL. The goal is to discover the hidden URL leaked within the application's frontend code and use the panel to delete the user `carlos`.

## 3. Tools Used
* Web Browser (Developer Tools / View Page Source)

## 4. Step-by-Step Methodology

1. Accessed the lab environment's home page. Right-clicked the page and selected "View Page Source" (or inspected the main `GET /` request in Burp Suite's HTTP history).
   
   <img width="1509" height="545" alt="image" src="https://github.com/user-attachments/assets/8a5d5165-a10e-49bb-9968-6a7aa2f07413" />

   *Figure 1 - The browser's "View Page Source" tab displaying the HTML of the home page.*

2. Analyzed the HTML source code, looking for hidden links or scripts. Discovered a JavaScript block that checks if a user is an admin and inadvertently leaks the unpredictable URL for the admin panel (e.g., `/admin-xxxxxx`).
   
   <img width="1515" height="673" alt="image" src="https://github.com/user-attachments/assets/ff98d38f-372b-4ba5-91e1-8be0abc8d4b9" />

   *Figure 2 - Highlighting the JavaScript code block that explicitly discloses the unpredictable admin URL.*

3. Copied the discovered directory path and appended it to the lab's base URL in the browser. The application loaded the admin panel directly, failing to enforce any backend authentication or authorization checks.
   
   

   <img width="1910" height="943" alt="image" src="https://github.com/user-attachments/assets/9ba8ff08-7859-4b33-b5af-5264f7188a6f" />

   *Figure 3 - The browser successfully loading the unprotected administrator panel using the leaked URL.*

4. Located the user `carlos` within the admin interface and clicked the "Delete" link. The server processed the deletion, successfully solving the lab.
   
   <img width="1902" height="539" alt="image" src="https://github.com/user-attachments/assets/5c11bba3-d94e-4e02-bf45-f814f59a0002" />

   *Figure 4 - The admin panel showing the "User deleted successfully" message, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```http
/admin-[DISCOVERED_STRING]
