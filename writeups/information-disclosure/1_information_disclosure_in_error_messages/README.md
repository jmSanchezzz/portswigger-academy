# Information disclosure in error messages

## 1. Lab Information
**Title:** Lab: Information disclosure in error messages  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Information Disclosure

## 2. Lab Objective
Exploit a vulnerability where the application handles unexpected input poorly, generating a verbose error message that reveals the vulnerable version of a third-party framework being used. The goal is to trigger this exception, obtain the framework version number from the stack trace, and submit it to solve the lab.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Proxy and Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and opened a specific product page. Switched to Burp Suite, navigated to **Proxy > HTTP history**, and located the `GET` request containing the `productId` parameter (e.g., `GET /product?productId=1`). Sent this request to Burp Repeater.
   
   <img width="1905" height="938" alt="image" src="https://github.com/user-attachments/assets/b822aebf-86b6-40b8-8563-c318fb97303c" />

   *Figure 1 - Burp Suite HTTP history showing the GET request for a product page.*

2. In Burp Repeater, modified the value of the `productId` parameter from an expected integer to an unexpected string data type (e.g., changing `productId=1` to `productId="example"`).
   
   
   <img width="1173" height="382" alt="image" src="https://github.com/user-attachments/assets/20efa485-08be-42b4-ba0e-df616bbd4b4a" />

   *Figure 2 - Burp Repeater showing the modified GET request with a string payload injected into the productId parameter.*

3. Clicked "Send." Because the application failed to handle the unexpected data type gracefully, it threw an unhandled exception. Scrolled through the server's response and observed a full debug stack trace. Identified that the verbose error message explicitly leaked the underlying framework and its specific version (Apache Struts 2 2.3.31). Copied this version number.
   
   <img width="1176" height="380" alt="image" src="https://github.com/user-attachments/assets/3180dd38-0fe8-48d3-aedf-aad6c1dbb545" />

   *Figure 3 - The server response returning a verbose stack trace, highlighting the leaked Apache Struts version number.*

4. Returned to the lab environment in the web browser. Clicked the "Submit solution" button, pasted the extracted version number (`2 2.3.31`) into the input field, and submitted it to successfully solve the lab.
   
   <img width="556" height="275" alt="image" src="https://github.com/user-attachments/assets/545b2b0e-ec8e-4b69-8456-9b26f712c9b0" />
   <img width="1901" height="243" alt="image" src="https://github.com/user-attachments/assets/fac616d9-86f9-4091-8e17-f2d8da4ab2b9" />

   *Figure 4 - Submitting the exfiltrated framework version, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
**URL Parameter Injection**
```http
?productId="example"
```

## 6. Mitigation / Remediation
To prevent information disclosure via error messages, applications must implement robust, standardized error handling and disable debug features in production environments.
* **Generic Error Messages:** Configure the web server and application framework to return generic, non-informative error messages (e.g., "An unexpected error occurred") to end users.
* **Disable Debug Mode:** Ensure that all debug modes, verbose logging, and stack trace rendering features are strictly disabled in production environments. Detailed error logs should only be written to secure, internal server files that are completely inaccessible from the client side.
* **Input Validation:** Implement strict input validation and type checking (e.g., ensuring `productId` is strictly an integer) so that unexpected data types are caught and handled gracefully before they reach sensitive backend components.
