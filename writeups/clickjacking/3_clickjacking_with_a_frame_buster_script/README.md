# Clickjacking with a frame buster script

## 1. Lab Information
**Title:** Lab: Clickjacking with a frame buster script  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Clickjacking (UI Redressing)

## 2. Lab Objective
Bypass a client-side frame buster script using the HTML5 `sandbox` attribute and conduct a clickjacking attack that frames the account page, tricking the victim into submitting a prefilled form to change their email address.

## 3. Tools Used
* Web Browser
* PortSwigger Exploit Server

## 4. Step-by-Step Methodology

1. Accessed the lab environment and logged into the application using the provided credentials (`wiener:peter`). Navigated to the "My account" page. The application utilizes a frame buster script (typically implemented using JavaScript like `if (top != self) top.location.href = self.location.href;`) to prevent malicious framing.
   
   <img width="1026" height="494" alt="image" src="https://github.com/user-attachments/assets/7de93bf3-4443-41b0-9840-c3d1d9a55df5" />

   *Figure 1 - The user account page containing the target "Update email" functionality.*

2. Navigated to the Exploit Server to construct the payload. To neutralize the frame buster, the payload utilizes the HTML5 `sandbox` attribute within the `iframe`. By setting `sandbox="allow-forms"` and explicitly omitting `allow-top-navigation` or `allow-scripts`, the browser blocks the frame buster script from executing its redirection while still allowing the necessary email form to be submitted.
   
   

   <img width="1534" height="489" alt="image" src="https://github.com/user-attachments/assets/efd4feab-d5b9-4584-803c-654f4b2cbacf" />

   *Figure 2 - The Exploit Server body field containing the initial clickjacking HTML template, notably featuring the sandbox="allow-forms" attribute.*

3. Prefilled the form by appending the URL parameter `?email=hacker@evil.com` to the iframe's `src` attribute. Adjusted the CSS parameters to align the elements, setting the iframe opacity to `0.1` temporarily. Set the iframe dimensions (width: `500px`, height: `700px`) and iteratively tweaked the `top` (e.g., `385px`) and `left` (e.g., `80px`) of the decoy div until "Test me" sat exactly underneath the target "Update email" button.
   
   <img width="815" height="893" alt="image" src="https://github.com/user-attachments/assets/448ea9fd-b608-4d85-bb2d-67e12af730a9" />

   *Figure 3 - The browser displaying the locally viewed exploit with 0.1 opacity, showing the decoy "Test me" text perfectly aligned beneath the target "Update email" button.*

4. Once the alignment was confirmed, finalized the payload by changing the decoy text to "Click me" and setting the iframe's opacity to `0.0001` to make it completely transparent.
   
   <img width="1531" height="483" alt="image" src="https://github.com/user-attachments/assets/5ed03fe8-5a2f-4af8-8152-dc93ddbdd578" />

   *Figure 4 - The finalized payload in the Exploit Server with the opacity updated to make the iframe invisible.*

5. Verified that the prefilled email address in the payload did not match the current account email. Clicked "Store" to save the payload, and then clicked "Deliver exploit to victim". The victim's browser loaded the sandboxed iframe (blocking the frame buster), prepopulated the email address, and the victim inadvertently clicked the decoy to solve the lab.
   
   <img width="1902" height="258" alt="image" src="https://github.com/user-attachments/assets/68b3e2b3-3601-4281-b42f-d2a5a9b1fa4a" />

   *Figure 5 - The "Congratulations, you solved the lab!" banner after delivering the exploit.*

## 5. The Payload
```html
<style>
    iframe {
        position:relative;
        width: 500px;
        height: 700px;
        opacity: 0.0001;
        z-index: 2;
    }
    div {
        position:absolute;
        top: 385px;
        left: 80px;
        z-index: 1;
    }
</style>
<div>Click me</div>
<iframe sandbox="allow-forms" src="[https://YOUR-LAB-ID.web-security-academy.net/my-account?email=hacker@evil.com](https://YOUR-LAB-ID.web-security-academy.net/my-account?email=hacker@evil.com)"></iframe>
