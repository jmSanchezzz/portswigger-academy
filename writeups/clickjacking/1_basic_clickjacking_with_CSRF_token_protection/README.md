# Basic clickjacking with CSRF token protection

## 1. Lab Information
  **Title:** Lab: Basic clickjacking with CSRF token protection  
  **Difficulty Level:** Apprentice  
  **Vulnerability Category:** Clickjacking (UI Redressing)

## 2. Lab Objective
Exploit a clickjacking vulnerability to bypass CSRF token protection. The goal is to craft a malicious HTML page that invisibly frames the user's account page and tricks the victim into clicking the "Delete account" button.

## 3. Tools Used
* Web Browser
* PortSwigger Exploit Server

## 4. Step-by-Step Methodology

1. Accessed the lab environment and logged into the application using the provided credentials (`wiener:peter`). Navigated to the "My account" page to identify the target functionality: the "Delete account" button.
   
   <img width="1902" height="921" alt="image" src="https://github.com/user-attachments/assets/c7b45c8f-141f-4957-a73e-8941dd008a6e" />

   *Figure 1 - The user account page showing the target "Delete account" button.*

2. Navigated to the Exploit Server to construct the clickjacking payload. The attack relies on CSS positioning to overlay a transparent iframe of the target application directly on top of a visible, harmless-looking decoy element (a div with the text "Test me" or "Click me").
   
   

   <img width="1535" height="460" alt="image" src="https://github.com/user-attachments/assets/d3dfe43e-4b6a-47b4-a1ef-007bc468b0a3" />

   *Figure 2 - The Exploit Server body field containing the initial clickjacking HTML template with the opacity set to 0.1 for testing.*

3. Adjusted the CSS parameters to align the invisible elements. Set the iframe opacity to `0.1` temporarily to see both layers. Used the "Store" and "View exploit" buttons to iteratively tweak the `top` (e.g., `300px`) and `left` (e.g., `60px`) of the decoy div until it sat exactly underneath the "Delete account" button of the semi-transparent iframe.
   
   <img width="904" height="674" alt="image" src="https://github.com/user-attachments/assets/6d2f4fdd-95f8-458b-ae8c-ee0f06ceeca4" />

   *Figure 3 - The browser displaying the locally viewed exploit with 0.1 opacity, showing the decoy "Click me" text perfectly aligned beneath the target "Delete account" button.*

4. Once the alignment was perfect, finalized the payload by changing the decoy text to "Click me" and setting the iframe's opacity to a near-invisible value (e.g., `0.0001`).
   
   <img width="1523" height="472" alt="image" src="https://github.com/user-attachments/assets/d175882d-ed46-452d-bb99-5e6ddf87333b" />

   *Figure 4 - The finalized payload in the Exploit Server with the opacity updated to make the iframe completely transparent.*

5. Clicked "Store" to save the final payload, and then clicked "Deliver exploit to victim". The simulated victim, using Chrome, was tricked into clicking the decoy text, which seamlessly clicked the "Delete account" button on the hidden iframe above it, solving the lab.
   
   <img width="1918" height="288" alt="image" src="https://github.com/user-attachments/assets/94689d21-bb75-416d-b560-8af3e290fe3b" />

   *Figure 5 - The "Congratulations, you solved the lab!" banner after delivering the clickjacking exploit.*

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
        top: 300px;
        left: 60px;
        z-index: 1;
    }
</style>
<div>Click me</div>
<iframe src="[https://YOUR-LAB-ID.web-security-academy.net/my-account](https://YOUR-LAB-ID.web-security-academy.net/my-account)"></iframe>
