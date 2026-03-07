# OS command injection, simple case

## 1. Lab Information
**Title:** OS command injection, simple case  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** OS Command Injection

## 2. Lab Objective
Exploit an OS command injection vulnerability in the product stock checker. The application executes a shell command containing user-supplied product and store IDs and returns the raw output. The goal is to execute the `whoami` command to determine the name of the current user.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment, navigated to a product page, and clicked the "Check stock" button. Switched to Burp Suite, located the resulting `POST /product/stock` request in the HTTP history, and sent it to Burp Repeater.
   
   <img width="1870" height="910" alt="image" src="https://github.com/user-attachments/assets/ecf944d3-b23f-49b8-9384-ec5fc0cecb5b" />

   *Figure 1 - Burp Suite HTTP history showing the POST request to /product/stock being sent to Repeater.*

2. In Burp Repeater, analyzed the request body containing the `productId` and `storeId` parameters. Recognized that if the application passes these directly to a system shell command (e.g., `stockcheck.sh <productId> <storeId>`), the input can be broken out of using shell metacharacters.
   
   <img width="1493" height="572" alt="image" src="https://github.com/user-attachments/assets/945e1b58-dc04-49e8-a978-60913f59dc53" />


   *Figure 2 - Burp Repeater showing the original stock check request parameters.*

3. Modified the `storeId` parameter to inject a new shell command using the pipe operator (`|`). Changed the value to `1|whoami`. The pipe tells the shell to execute the first command (the stock check), pipe its output (or fail gracefully), and then execute the second command (`whoami`).
   
   
   <img width="1493" height="331" alt="image" src="https://github.com/user-attachments/assets/ec749d95-38db-47d2-aa67-ad76354c635a" />

   *Figure 3 - Burp Repeater showing the modified storeId parameter with the injected whoami command.*

4. Clicked "Send". The server evaluated the injected payload, executed the `whoami` command at the operating system level, and reflected the raw output (the name of the current user) directly in the HTTP response, successfully solving the lab.
   
   <img width="1489" height="322" alt="image" src="https://github.com/user-attachments/assets/135633fc-eb99-491b-8e3e-587ae83ed84e" />
   <img width="1902" height="255" alt="image" src="https://github.com/user-attachments/assets/e65129b2-f553-4273-9bfe-012f4e9f01e2" />

   *Figure 4 - The HTTP response displaying the output of the whoami command, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```http
storeId=1|whoami
