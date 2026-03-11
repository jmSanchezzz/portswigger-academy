# Source code disclosure via backup files

## 1. Lab Information
**Title:** Lab: Source code disclosure via backup files  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Information Disclosure

## 2. Lab Objective
Exploit an information disclosure vulnerability where the application leaks sensitive backup files in a hidden directory. The goal is to manually discover this directory, access the leaked Java source code, extract a hard-coded database password, and submit it to solve the lab.

## 3. Tools Used
* Web Browser

## 4. Step-by-Step Methodology

1. Accessed the lab environment. In the web browser's address bar, appended `/robots.txt` to the base URL to check for any hidden directories the site administrator might be trying to hide from search engine crawlers.
   
   <img width="1920" height="245" alt="image" src="https://github.com/user-attachments/assets/38894db9-ebbb-4cf2-be48-c81f1fad5554" />

   *Figure 1 - Accessing the /robots.txt file and discovering the disallowed /backup directory.*

2. Observed that the `robots.txt` file explicitly listed `Disallow: /backup`. Manually navigated to this hidden directory by appending `/backup` to the lab's base URL.
   
   <img width="1154" height="312" alt="image" src="https://github.com/user-attachments/assets/dfe601bd-4685-485e-80f9-b264cc207439" />

   *Figure 2 - Navigating to the /backup directory and viewing the exposed directory listing.*

3. The server had directory listing enabled, revealing a file named `ProductTemplate.java.bak`. Clicked the file link to view its contents.
   
   <img width="1913" height="1013" alt="image" src="https://github.com/user-attachments/assets/f57833b9-dccc-429f-9a21-837d1e7ef65a" />

   *Figure 3 - Accessing the exposed ProductTemplate.java.bak backup file.*

4. Reviewed the leaked Java source code. Located the `ConnectionBuilder` class and identified the hard-coded PostgreSQL database credentials. Copied the value assigned to the password variable.
   
   <img width="913" height="284" alt="image" src="https://github.com/user-attachments/assets/0e9a2549-5773-4b69-886c-a94821ca3eb4" />

   *Figure 4 - The leaked source code highlighting the hard-coded database password.*

5. Navigated back to the main lab environment page. Clicked the "Submit solution" button, pasted the extracted database password into the input field, and submitted it to successfully solve the lab.
   
   <img width="561" height="274" alt="image" src="https://github.com/user-attachments/assets/4d8c8261-7962-4b35-b87b-baee5f521450" />
   <img width="1900" height="242" alt="image" src="https://github.com/user-attachments/assets/3984d161-fa70-494d-8357-4a4fd23ebc40" />

   *Figure 5 - Submitting the exfiltrated database password, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
**Discovered Paths**
```http
/robots.txt
/backup/ProductTemplate.java.bak
```

## 6. Mitigation / Remediation
To prevent source code and sensitive data disclosure, applications must implement secure deployment practices and strict access controls.
* **Remove Backup Files:** Never deploy backup files (e.g., `.bak`, `.old`, `.orig`) or development artifacts to a production web server. Ensure deployment pipelines only transfer necessary compiled code and production-ready assets.
* **Disable Directory Listing:** Configure the web server to disable automatic directory listings. If a user navigates to a directory without a default index file, the server should return a 403 Forbidden error rather than listing the directory contents.
* **Remove Hard-Coded Secrets:** Never hard-code sensitive information such as database passwords, API keys, or cryptographic secrets directly into the source code. Utilize environment variables or secure secret management services to handle sensitive configurations.
