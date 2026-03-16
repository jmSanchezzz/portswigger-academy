# Detecting NoSQL injection

## 1. Lab Information
**Title:** Lab: Detecting NoSQL injection  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** NoSQL Injection

## 2. Lab Objective
Exploit a NoSQL injection vulnerability in a product category filter powered by a MongoDB database. The goal is to identify that the application dynamically evaluates user input as JavaScript, test boolean conditions to map the vulnerability, and inject an "always true" payload to bypass the filter and display unreleased products.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Proxy - HTTP History and Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and clicked on a product category filter "Gifts" to establish a baseline of normal application behavior and capture the request.
   
   <img width="1901" height="913" alt="Image" src="https://github.com/user-attachments/assets/757096a7-bb04-4913-b085-bd2d7d70379b" />

   *Figure 1 - Browsing the application and applying a category filter to capture the routing logic.*

2. Switched to Burp Suite and navigated to **Proxy > HTTP history**. Located the `GET /filter?category=Gifts` request. Right-clicked it and selected "Send to Repeater". In Repeater, appended a single quote (`'`) to the category parameter (`category=Gifts'`) and clicked "Send". Observed a JavaScript syntax error in the response, indicating the input was breaking out of a string context.
   
   <img width="1491" height="713" alt="Image" src="https://github.com/user-attachments/assets/454acb8a-c919-4080-9f7e-d8a4e60d1c13" />

   *Figure 2 - Injecting a single quote into the category parameter and triggering a server-side syntax error.*

3. To verify if the server was actively evaluating the input as JavaScript, submitted a valid string concatenation payload: `Gifts'+'`. Used Burp's `Ctrl-U` shortcut to URL-encode the payload (becoming `Gifts'%2b'`). The server returned a `200 OK` with the normal "Gifts" products, confirming that server-side JavaScript evaluation was occurring.
   
   <img width="1496" height="757" alt="Image" src="https://github.com/user-attachments/assets/e78e0b9e-a0be-4bae-a105-47efd67ac3a8" />

   *Figure 3 - Successfully executing a string concatenation payload to prove code evaluation.*

4. Proceeded to test boolean conditions to see if the query logic could be manipulated. Sent a false condition: `Gifts' && 0 && 'x` (URL-encoded). The server returned zero products. Then sent a true condition: `Gifts' && 1 && 'x` (URL-encoded). The server returned the "Gifts" products. This confirmed full control over the query logic.
   
   <img width="1490" height="760" alt="Image" src="https://github.com/user-attachments/assets/f0750098-e49d-41bc-bbb2-8f275bac14f1" />
   <img width="1491" height="708" alt="Image" src="https://github.com/user-attachments/assets/0db009ac-9670-4095-925d-fb15eba5d1a0" />

   *Figure 4 - Proving boolean injection by manipulating the query to return empty or populated results.*

5. Crafted the final payload to force the database to return all records, bypassing the "released" status check. Submitted an OR condition that always evaluates to true: `Gifts'||1||'` URL-encoded to `Gifts'%7c%7c1%7c%7c'`. Clicked "Send".
   
   <img width="1492" height="296" alt="Image" src="https://github.com/user-attachments/assets/509f7310-fca9-49a1-990f-da93fe00df6a" />

   *Figure 5 - Injecting the "always true" OR condition into the category parameter via Burp Repeater.*

6. Right-clicked the successful response in Burp Repeater and selected **Show response in browser**. Copied the generated URL, pasted it into the web browser, and pressed Enter. The application rendered all products, including the hidden unreleased items, successfully solving the lab.
   
   <img width="1899" height="920" alt="Image" src="https://github.com/user-attachments/assets/7ad88b2a-6e6b-4fe9-92c4-0a2d57ed44ef" />

   *Figure 6 - Viewing the unreleased products in the browser, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
**NoSQL "Always True" Boolean Injection (URL Encoded)**
> `category=Gifts'%7c%7c1%7c%7c'`
> `*(Decoded: Gifts'||1||')*`

## 6. Mitigation / Remediation
To prevent NoSQL injection, applications must avoid evaluating dynamic user input as code and strictly separate data from queries.
* **Avoid JavaScript Execution:** Do not use operators that execute JavaScript expressions on the server side, such as MongoDB's `$where` operator. Rely on standard, safe query operators instead.
* **Use Strongly Typed Interfaces:** Ensure that the application framework or database driver securely maps user input to strongly typed objects (e.g., using Mongoose in Node.js). Reject input that does not match the expected data type (e.g., passing an object or array when a string is expected).
* **Input Validation:** Implement strict allowlisting for parameters like category filters, ensuring only known, valid categories can be queried.
