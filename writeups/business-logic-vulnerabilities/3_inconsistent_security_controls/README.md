# Inconsistent security controls

## 1. Lab Information
**Title:** Lab: Inconsistent security controls   
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Business Logic Vulnerabilities

## 2. Lab Objective
Exploit inconsistent security controls where the application applies strict validation during account registration but fails to enforce the same rules during account updates. The goal is to register a standard account, exploit the email update feature to spoof a corporate `@dontwannacry.com` address, gain administrative privileges, and delete the user `carlos`.

## 3. Tools Used
* Web Browser
* Lab Email Client

## 4. Step-by-Step Methodology

1. Accessed the lab environment. Manually appended `/admin` to the base URL in the address bar to check for an administrative interface. The server returned an "Admin interface only available if logged in as a DontWannaCry user" message, revealing the target corporate domain.
   
   <img width="1893" height="483" alt="image" src="https://github.com/user-attachments/assets/1ba2490b-b096-4b8f-8349-dfff75fed8d0" />

   *Figure 1 - Accessing the /admin endpoint and discovering the target DontWannaCry user requirement.*

2. Navigated to the "Register" page. Opened the lab's simulated "Email client" in a new tab to obtain the assigned temporary email domain (`@exploit-0a05003c04f9bda680a78fe3015a0094.exploit-server.net`). Registered a new account using an arbitrary username and this temporary email address.
   
   <img width="1013" height="623" alt="image" src="https://github.com/user-attachments/assets/9b163b5c-e023-40f9-92ec-5f2fc6ff2479" />

   *Figure 2 - Registering a standard user account using the provided temporary email client domain.*

3. Returned to the Email client, located the registration confirmation email, and clicked the verification link. Logged into the application using the newly created credentials and navigated to the "My account" page.
   
   <img width="1519" height="566" alt="image" src="https://github.com/user-attachments/assets/95b29d41-94b1-41d4-9164-e19565244b77" />

   *Figure 3 - Verifying the standard account via the Email client and logging in.*

4. On the "My account" page, identified the "Update email" form. Attempted to bypass the initial registration restrictions by entering a spoofed corporate email address `admin@dontwannacry.com` and submitting the form.
   
   

   <img width="1008" height="499" alt="image" src="https://github.com/user-attachments/assets/a91acd77-3965-429c-b2a1-7d7c6f50d5ff" />

   *Figure 4 - Updating the account email to a spoofed admin@dontwannacry.com address.*

5. The application processed the update successfully without sending a verification link to the new address. Refreshed the page and observed that an "Admin panel" link dynamically appeared in the navigation bar, confirming that administrative privileges were automatically granted based purely on the modified email domain.
   
   <img width="1721" height="805" alt="image" src="https://github.com/user-attachments/assets/578762de-1bd3-4018-9a3e-0ab846c5a7ea" />

   *Figure 5 - The My Account page displaying the new Admin panel link after the successful email update.*

6. Clicked the "Admin panel" link (navigating to `/admin`). Located the target user `carlos` in the user list and clicked the "Delete" button. The server processed the deletion, successfully solving the lab.
   
   <img width="1901" height="629" alt="image" src="https://github.com/user-attachments/assets/1c46b2dd-be84-44bb-93be-a4075182379d" />

   *Figure 6 - Deleting the user carlos from the Admin panel, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
**Spoofed Email Address Update**
> `admin@dontwannacry.com`

## 6. Mitigation / Remediation
To prevent inconsistent security control vulnerabilities, applications must enforce business logic rules uniformly across all related endpoints.
* **Consistent Validation:** Any validation rules applied during user registration (such as restricting certain email domains) must be strictly enforced during profile updates.
* **Mandatory Email Verification:** Whenever a user attempts to change their email address, the application must require the user to verify ownership of the new address by clicking a unique, cryptographically secure link sent to that specific inbox before applying the change.
* **Secure Privilege Assignment:** Administrative privileges should never be dynamically assigned based on user-controllable data like an email domain. Privileges must be explicitly granted and managed by authorized administrators and stored securely in the backend database (e.g., using a `role_id` column).
