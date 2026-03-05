# Reflected XSS into a JavaScript string with angle brackets HTML encoded

## 1. Lab Information
**Title:** Lab: Reflected XSS into a JavaScript string with angle brackets HTML encoded  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Reflected Cross-Site Scripting (XSS)

## 2. Lab Objective
Perform a cross-site scripting attack that breaks out of a JavaScript string and calls the `alert` function, bypassing the fact that the application HTML-encodes angle brackets.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition

## 4. Step-by-Step Methodology

1. Accessed the lab environment, entered a random alphanumeric string (e.g., "test1234") into the search box, and submitted the search. Intercepted this request using Burp Suite and sent it to the Repeater tab.
   
   <img width="1358" height="499" alt="image" src="https://github.com/user-attachments/assets/481346f8-74c9-4519-91d9-1231cba5bbeb" />

   *Figure 1 - Burp Suite Proxy showing the intercepted search request.*

2. Analyzed the HTTP response in Burp Repeater to observe how the application handles the input. Discovered that the search term was reflected directly inside a JavaScript string variable within a `<script>` block. Observed that angle brackets (`<` and `>`) were safely HTML-encoded, meaning it was not possible to close the `<script>` tag to inject new HTML.
   
   <img width="1356" height="368" alt="image" src="https://github.com/user-attachments/assets/b6f9770d-92de-4362-b4d5-152c60ec9396" />

   *Figure 2 - Burp Suite Repeater response showing the search term reflected inside the quoted JavaScript string.*

3. Crafted a payload to break out of the JavaScript string context. Replaced the search input in the URL parameter with the payload `'-alert(1)-'`. (The first single quote `'` closes the existing string, the minus `-` acts as an arithmetic operator to separate the string from the injected `alert(1)` function, and the trailing `-'` ensures the rest of the original JavaScript remains syntactically valid).
   
   <img width="1361" height="393" alt="image" src="https://github.com/user-attachments/assets/145314bf-4343-4f37-a50a-a9c44f3e1878" />

   *Figure 3 - Burp Suite Repeater showing the injected payload escaping the string and executing the alert function.*

4. Verified the technique by applying the payload to the browser URL. When the page loaded, the browser executed the modified JavaScript block, successfully triggering the `alert(1)` function and solving the lab.
   
   <img width="1920" height="919" alt="image" src="https://github.com/user-attachments/assets/0c239e63-0c5f-4d25-a2f8-680f4c43671c" />

   *Figure 4 - The browser displaying the executed JavaScript alert pop-up box and the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```javascript
'-alert(1)-'
