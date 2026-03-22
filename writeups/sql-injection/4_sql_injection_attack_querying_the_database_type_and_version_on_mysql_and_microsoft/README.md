# SQL injection attack, querying the database type and version on MySQL and Microsoft

## 1. Lab Information
**Title:** Lab: SQL injection attack, querying the database type and version on MySQL and Microsoft  
**Difficulty Level:** Practitioner  
**Vulnerability Category:** SQL Injection

## 2. Lab Objective
Exploit a SQL injection vulnerability in the product category filter using a UNION attack on a MySQL or Microsoft SQL Server backend. The goal is to determine the column structure and inject a payload to retrieve and display the database version string.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Proxy - HTTP History and Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and clicked on a product category filter "Tech Gifts" to capture the target request.
   
   <img width="1899" height="919" alt="image" src="https://github.com/user-attachments/assets/3ca13dab-e866-40f4-9c94-04aadf51f7bf" />

   *Figure 1 - Browsing the application and clicking a category filter to capture the routing logic.*

2. Switched to Burp Suite and navigated to **Proxy > HTTP history**. Located the `GET /filter?category=Tech+Gifts` request. Right-clicked the request and selected "Send to Repeater" to begin probing for injection points.
   
   <img width="1492" height="435" alt="image" src="https://github.com/user-attachments/assets/07e6c122-6445-4ffa-b5db-21f3a10d41c1" />

   *Figure 2 - Isolating the target GET request in Burp HTTP history.*

3. In Burp Repeater, tested the `category` parameter to determine the number of columns and their data types. Unlike Oracle, MySQL and Microsoft SQL Server do not require a `FROM` clause for selecting constants. Injected the payload `'+UNION+SELECT+'abc','def'#` to confirm the query returns two text-compatible columns. The `#` character is used here as a comment to nullify the rest of the original query.
   
   <img width="1495" height="765" alt="image" src="https://github.com/user-attachments/assets/b6037c9d-7b2e-4fd7-95f9-a99a29382fac" />

   *Figure 3 - Confirming two text columns using MySQL/MSSQL comment syntax.*

4. After confirming the two-column structure, constructed the final payload to extract the database version. Both MySQL and Microsoft SQL Server use the global variable `@@version` to store this information. Modified the payload to select `@@version` in the first column and `NULL` in the second: `'+UNION+SELECT+@@version,+NULL#`. Clicked "Send".
   
   <img width="1500" height="386" alt="image" src="https://github.com/user-attachments/assets/c8f6d9fe-87ef-4552-8e91-5d6f99ea43ae" />

   *Figure 4 - Injecting the final payload to extract the database version variable.*

5. Reviewed the HTTP response and verified that the version string (e.g., `8.0.35-0ubuntu0.20.04.1`) was successfully rendered within the product table in the HTML. The lab was solved.
   
   <img width="1900" height="822" alt="image" src="https://github.com/user-attachments/assets/d6a32c1e-1667-4da7-bd08-f7d6bb6fd071" />

   *Figure 5 - The database version string successfully displayed in the response, followed by the lab completion banner.*

## 5. The Payload
**MySQL/MSSQL Version Extraction (UNION Attack)**
> `category=Lifestyle'+UNION+SELECT+@@version,+NULL#`

## 6. Mitigation / Remediation
To prevent SQL injection vulnerabilities, applications must strictly separate untrusted user input from the executable database query.
* **Use Parameterized Queries (Prepared Statements):** This is the primary defense. By using placeholders, the database engine treats input as data and never as executable SQL commands, regardless of the database type.
* **Input Validation:** Implement a strict allowlist for parameters. For a category filter, the application should only accept pre-defined category strings and reject any input containing special characters like `'`, `#`, or `--`.
