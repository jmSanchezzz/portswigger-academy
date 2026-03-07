# Unprotected admin functionality

## 1. Lab Information
**Title:** Lab: Unprotected admin functionality  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Access Control (Broken Access Control)

## 2. Lab Objective
Exploit a broken access control vulnerability where the application's administrative panel is completely unprotected. The goal is to discover the hidden admin panel URL via the `robots.txt` file and delete the user `carlos`.

## 3. Tools Used
* Web Browser

## 4. Step-by-Step Methodology

1. Accessed the lab environment. Appended `/robots.txt` to the base URL in the browser to view the site's web crawler instructions.
   
   <img width="1920" height="1031" alt="image" src="https://github.com/user-attachments/assets/61bffe49-5ab3-4b76-b7a1-981488987d96" />

   *Figure 1 - The browser displaying the contents of the robots.txt file, revealing the disallowed path.*

2. Analyzed the `robots.txt` file and observed a `Disallow` rule pointing to `/administrator-panel`. This inadvertently disclosed the location of the hidden admin interface.
   
   <img width="889" height="328" alt="image" src="https://github.com/user-attachments/assets/a4ef6da7-8701-4be2-b540-3c78be4be2ee" />

   *Figure 2 - Highlighting the exposed /administrator-panel directory in the robots.txt file.*

3. Appended `/administrator-panel` to the lab's base URL in the browser. The application loaded the admin panel directly, failing to request any authentication or verify authorization.
   
   <img width="1883" height="919" alt="image" src="https://github.com/user-attachments/assets/ba40f7cb-bcba-4fa5-8277-b48d86e34d4c" />

   *Figure 3 - The browser successfully loading the unprotected administrator panel.*

4. Located the user `carlos` within the admin interface and clicked the "Delete" link. The server processed the deletion, successfully solving the lab.
   
   <img width="1905" height="539" alt="image" src="https://github.com/user-attachments/assets/750e196c-61f5-47ed-9bec-601421e704ef" />

   *Figure 4 - The admin panel showing the "User deleted successfully" message, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```http
/administrator-panel
