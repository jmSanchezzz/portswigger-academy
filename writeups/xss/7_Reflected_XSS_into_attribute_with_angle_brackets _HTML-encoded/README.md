# Reflected XSS into attribute with angle brackets HTML-encoded

## 1. Lab Information
**Title:** Lab: Reflected XSS into attribute with angle brackets HTML-encoded  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Cross-Site Scripting (XSS)

## 2. Lab Objective
Perform a cross-site scripting attack by injecting an attribute to call the `alert` function, bypassing the fact that the application HTML-encodes angle brackets.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition

## 4. Step-by-Step Methodology

1. Accessed the lab environment, entered a random alphanumeric string (e.g., "test1234") into the search box, and submitted the search. Intercepted this request using Burp Suite and sent it to the Repeater tab.
   
   <img width="1284" height="587" alt="image" src="https://github.com/user-attachments/assets/d897a262-45fb-4cf6-aa8a-4f7a5ec88048" />

   *Figure 1 - Burp Suite Proxy showing the intercepted search request.*

2. Analyzed the HTTP response in Burp Repeater to see how the application handles the input. Observed that the random string was reflected directly inside a quoted attribute (specifically, the `value` attribute of the search `<input>` tag). However, any angle brackets (`<` and `>`) were safely HTML-encoded, meaning a standard `<script>` tag payload would not work.
   

   <img width="1470" height="361" alt="image" src="https://github.com/user-attachments/assets/e96cf6f3-f11a-4faf-ae7d-e4fed88ce3e9" />

   *Figure 2 - Burp Suite Repeater response showing the search term reflected inside the quoted value attribute.*

3. Crafted a payload to break out of the quoted attribute and inject a new JavaScript event handler without needing angle brackets. Replaced the search input in the URL parameter with the payload `"onmouseover="alert(1)`. (The double quote `"` closes the existing `value` attribute, and `onmouseover=` adds a new event listener to the element).
   
   <img width="1358" height="322" alt="image" src="https://github.com/user-attachments/assets/2b741cb6-f8aa-460e-ba80-e669527b8597" />

   *Figure 3 - Burp Suite Repeater showing the injected payload escaping the attribute and adding the onmouseover event.*

4. Verified the technique by applying the payload to the browser URL. When the page loaded, moved the mouse pointer over the search input field. This triggered the injected `onmouseover` event handler, successfully executing the `alert(1)` function and solving the lab.
   
   <img width="1893" height="909" alt="image" src="https://github.com/user-attachments/assets/f208d5cf-339c-4a8a-8e41-cf005431a1c3" />

   *Figure 4 - The browser displaying the executed JavaScript alert pop-up box upon hovering over the search bar, along with the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```html
"onmouseover="alert(1)
