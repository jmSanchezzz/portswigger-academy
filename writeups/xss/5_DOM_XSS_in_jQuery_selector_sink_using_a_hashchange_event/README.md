# DOM XSS in jQuery selector sink using a hashchange event

## 1. Lab Information
**Title:** Lab: DOM XSS in jQuery selector sink using a hashchange event  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** DOM-based Cross-Site Scripting (DOM XSS)

## 2. Lab Objective
Deliver a stored exploit to the victim that leverages a DOM-based cross-site scripting vulnerability. The attack must manipulate the `location.hash` property and exploit jQuery's `$()` selector function to successfully call the `print()` function in the victim's browser.

## 3. Tools Used
* Web Browser (with Developer Tools / Inspector)
* PortSwigger Exploit Server

## 4. Step-by-Step Methodology

1. Accessed the lab environment and used the browser's Developer Tools to inspect the home page's source code. Identified a vulnerable JavaScript block listening for a `hashchange` event. The script dynamically takes the value from the URL hash (`location.hash`) and passes it directly into a jQuery selector `$()` without any sanitization.
 
    <img width="1513" height="732" alt="image" src="https://github.com/user-attachments/assets/34e90e07-3e76-46f7-a656-27a10b6c0780" />

   *Figure 1 - Browser Developer Tools showing the vulnerable JavaScript code that passes the URL hash into the jQuery selector.*

2. Clicked the "Go to exploit server" button provided in the lab banner to access the environment where the payload will be hosted and delivered to the simulated victim.
   
   <img width="1918" height="1031" alt="image" src="https://github.com/user-attachments/assets/7577229a-a7cf-4642-9a85-d8fb464a0683" />

   *Figure 2 - The PortSwigger Exploit Server interface.*

3. Crafted a malicious payload designed to trigger the `hashchange` event without user interaction. In the Body section of the exploit server, entered an iframe payload: `<iframe src="https://YOUR-LAB-ID.web-security-academy.net/#" onload="this.src+='<img src=x onerror=print()>'"></iframe>`. (This iframe first loads the vulnerable page with an empty hash, and then immediately appends the malicious XSS image payload to the URL upon loading, triggering the `hashchange` event and executing the `print()` function).
   <img width="1915" height="916" alt="image" src="https://github.com/user-attachments/assets/3352f0c5-a911-41e8-a413-ff9dd1a0c1ae" />

   *Figure 3 - The Exploit Server body field containing the malicious iframe payload.*

4. Clicked Store and then View exploit to test the payload locally. Verified that the browser's print dialog box opened, confirming the exploit worked. Finally, returned to the exploit server and clicked Deliver exploit to victim, successfully solving the lab.
   
   <img width="1908" height="979" alt="image" src="https://github.com/user-attachments/assets/1b1cef83-e476-4b8b-b001-408b89122d4d" />
   <img width="1886" height="258" alt="image" src="https://github.com/user-attachments/assets/1bac6880-770e-497c-9a67-229efd055d73" />

   *Figure 4 - The browser displaying the triggered print dialog box and the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```html
<iframe src="[https://YOUR-LAB-ID.web-security-academy.net/#](https://YOUR-LAB-ID.web-security-academy.net/#)" onload="this.src+='<img src=x onerror=print()>'"></iframe>
