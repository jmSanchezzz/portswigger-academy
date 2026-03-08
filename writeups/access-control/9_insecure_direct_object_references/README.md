# Insecure direct object references

## 1. Lab Information
**Title:** Lab: Insecure direct object references  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Access Control (Insecure Direct Object Reference / IDOR)

## 2. Lab Objective
Exploit an Insecure Direct Object Reference (IDOR) vulnerability where user chat logs are stored directly on the server's file system using predictable, incrementing filenames. The goal is to manipulate the file path in the URL to access a previous chat transcript, extract the password for the user `carlos`, and log into his account.

## 3. Tools Used
* Web Browser

## 4. Step-by-Step Methodology

1. Accessed the lab environment and navigated to the "Live chat" tab. Sent a test message in the chat window and clicked the "View transcript" button to download the chat history.
   
   <img width="1897" height="914" alt="image" src="https://github.com/user-attachments/assets/b12817db-ef39-4b3f-87bf-131ba8713a05" />

   *Figure 1 - The Live chat interface showing the test message and the "View transcript" option.*

2. Analyzed the URL of the retrieved transcript in the browser's address bar. Observed that the application fetches chat logs using static, predictably named text files with incrementing numbers.
   
   <img width="1882" height="1030" alt="image" src="https://github.com/user-attachments/assets/97d4b654-37dc-4564-a948-4813ad53691a" />

   *Figure 2 - The browser's address bar revealing the predictable, sequential filename format used for chat transcripts.*

3. Modified the URL directly in the browser, changing the filename to `1.txt` to access the very first chat transcript recorded by the system. Pressed Enter to navigate to the new URL.
   
   

   <img width="1767" height="275" alt="image" src="https://github.com/user-attachments/assets/b18a3a29-50fe-4f57-82ee-be5a20bb7f86" />

   *Figure 3 - Modifying the URL parameter to target the static file 1.txt.*

4. Reviewed the contents of the `1.txt` transcript that the server returned. Discovered a sensitive conversation where the user `carlos` inadvertently disclosed his password to a support agent. Copied the exposed password.
   
   <img width="1264" height="355" alt="image" src="https://github.com/user-attachments/assets/ae175454-c4a2-4232-998c-98666d749676" />

   *Figure 4 - The contents of the 1.txt chat transcript, highlighting Carlos's disclosed password.*

5. Navigated back to the main lab page and clicked "My account". Authenticated using the username `carlos` and the exfiltrated password. The application granted access, successfully solving the lab.
   
   <img width="1903" height="711" alt="image" src="https://github.com/user-attachments/assets/29f4937e-32bc-42d2-ad71-7ba6fe23dca0" />

   *Figure 5 - Successfully logging into the application as carlos, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```text
/download-transcript/1.txt
