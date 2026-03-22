# SQL injection attack, querying the database type and version on Oracle

## 1. Lab Information
**Title:** Lab: SQL injection attack, querying the database type and version on Oracle  
**Difficulty Level:** Practitioner  
**Vulnerability Category:** SQL Injection

## 2. Lab Objective
Exploit a SQL injection vulnerability in the product category filter using a UNION attack. The goal is to determine the number of columns returned by the query and inject a payload to retrieve and display the Oracle database version string.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Proxy - HTTP History and Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and clicked on a product category filter (e.g., "Gifts") to capture the target request.
   
   <img width="1901" height="921" alt="image" src="https://github.com/user-attachments/assets/9d7fe0b0-e7a7-4ab6-8db5-d36f5da3dfdf" />
   
   *Figure 1 - Browsing the application and clicking a category filter to capture the routing logic.*

2. Switched to Burp Suite and navigated to **Proxy > HTTP history**. Located the `GET /filter?category=...` request. Right-clicked the request and selected "Send to Repeater" to test for SQL injection vulnerabilities.
   
   <img width="1492" height="495" alt="image" src="https://github.com/user-attachments/assets/ef480fdd-47fa-472f-b37f-b62c1dc73804" />

   *Figure 2 - Isolating the target GET request in Burp HTTP history.*

3. In Burp Repeater, tested the `category` parameter to determine the number of columns and data types returned by the original query. Since this is an Oracle database, every `SELECT` statement must include a `FROM` clause (using the built-in `dual` table). Injected the payload `'+UNION+SELECT+'abc','def'+FROM+dual--` to confirm the query returns two text columns.
   
   <img width="1487" height="708" alt="image" src="https://github.com/user-attachments/assets/2d1d88fd-6e59-422b-8642-9991202783fe" />

   *Figure 3 - Confirming the presence of two text-compatible columns using the Oracle 'dual' table.*

4. After mapping the column structure, constructed the final payload to extract the database version. On Oracle, version information is stored in the `v$version` table. Modified the payload to select the `BANNER` column from `v$version` for the first column, and `NULL` for the second: `'+UNION+SELECT+BANNER,+NULL+FROM+v$version--`. Clicked "Send".
   
   <img width="1483" height="388" alt="image" src="https://github.com/user-attachments/assets/45be8d87-f4b8-4434-adac-1a32c1d7416f" />

   *Figure 4 - Injecting the final payload to extract the Oracle version string.*

5. Reviewed the HTTP response and observed the Oracle database version string successfully rendered within the HTML table. Clicked "Show response in browser" to verify visually, successfully solving the lab.
   
   <img width="1902" height="909" alt="image" src="https://github.com/user-attachments/assets/b6810d96-d4d3-4c60-b9e0-fac79c9ec200" />

   *Figure 5 - The Oracle database version string successfully displayed in the response, followed by the lab completion banner.*

## 5. The Payload
**Oracle Version Extraction (UNION Attack)**
> `category=Gifts'+UNION+SELECT+BANNER,+NULL+FROM+v$version--`

## 6. Mitigation / Remediation
To prevent SQL injection vulnerabilities, applications must strictly separate untrusted user input from the executable database query.
* **Use Parameterized Queries (Prepared Statements):** This is the primary defense against SQL injection. The database driver ensures that user input is treated strictly as data (a literal value) and never as executable code, neutralizing any injected SQL syntax.
* **Input Validation:** Implement strict allowlisting for parameters like category filters, ensuring only known, valid categories can be passed to the backend logic.
