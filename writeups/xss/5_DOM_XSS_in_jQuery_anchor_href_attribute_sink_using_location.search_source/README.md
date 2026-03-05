# DOM XSS in jQuery anchor href attribute sink using location.search source

## 1. Lab Information
**Title:** DOM XSS in jQuery anchor href attribute sink using location.search source
**Difficulty Level:** Apprentice
**Vulnerability Category:** DOM-based Cross-Site Scripting (DOM XSS)

## 2. Lab Objective
Perform a DOM-based cross-site scripting attack by manipulating the `location.search` source to inject a malicious JavaScript pseudo-protocol into a jQuery anchor `href` sink, causing the "back" link to alert `document.cookie`.

## 3. Tools Used
* Web Browser (with Developer Tools / Inspector)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and navigated to the "Submit feedback" page. Observed the URL, specifically noting the `returnPath` query parameter.
   
   <img width="926" height="137" alt="image" src="https://github.com/user-attachments/assets/9ac91e4d-746b-4925-aeee-348392048e77" />

   *Figure 1 - The "Submit feedback" page and the URL containing the target returnPath parameter.*

2. To trace how the application handles the input, modified the `returnPath` parameter in the URL to a random alphanumeric string (e.g., `?returnPath=/test1234`) and hit Enter. Right-clicked the "Back" link on the page and selected "Inspect".
   
   <img width="1525" height="619" alt="image" src="https://github.com/user-attachments/assets/6bdb053e-2a6c-43a7-b298-867171f58a97" />

   *Figure 2 - Browser Developer Tools showing the random string reflected directly inside the href attribute of the anchor (`<a>`) tag.*

3. Identified that a jQuery script was dynamically taking the value from `location.search` (the `returnPath` parameter) and assigning it directly to the `href` attribute using the `attr()` function. To exploit this execution sink, crafted the payload `javascript:alert(document.cookie)` and replaced the `returnPath` value in the URL.
   
   <img width="1339" height="275" alt="image" src="https://github.com/user-attachments/assets/d0164798-b97c-43b8-bac6-b194a6febc92" />

   *Figure 3 - The URL modified with the injected JavaScript pseudo-protocol payload.*

4. Pressed Enter to reload the page with the malicious payload. Clicked the "Back" link. Because the `href` attribute was now populated with `javascript:...`, the browser executed the injected code instead of navigating to a new page, successfully displaying the session cookies and solving the lab.
   
   <img width="1917" height="1020" alt="image" src="https://github.com/user-attachments/assets/4f5bba22-d0c3-4fab-9823-bda1dcfd50a9" />
   <img width="1920" height="951" alt="image" src="https://github.com/user-attachments/assets/f3137a18-fe43-4a33-a3d4-d07540ed4df1" />

   *Figure 4 - The browser displaying the executed JavaScript alert containing the cookie data and the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```javascript
javascript:alert(document.cookie)
