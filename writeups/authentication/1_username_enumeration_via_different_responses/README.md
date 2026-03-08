# Username enumeration via different responses

## 1. Lab Information
**Title:** Lab: Username enumeration via different responses  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Authentication (Username Enumeration & Password Brute-Force)

## 2. Lab Objective
Exploit a flawed authentication mechanism that returns distinct error messages for valid and invalid usernames. The goal is to use Burp Intruder with a provided wordlist to enumerate a valid username, use a second Intruder attack to brute-force the password, and log into the compromised account.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Proxy and Intruder)

## 4. Step-by-Step Methodology



1. Accessed the lab environment and downloaded the provided wordlists for candidate usernames and passwords. Navigated to the login page and submitted a dummy username and password to generate a login request. Located the `POST /login` request in Burp Suite's HTTP history and sent it to Burp Intruder.
   
   <img width="1881" height="941" alt="image" src="https://github.com/user-attachments/assets/8cd96c76-0e2b-4647-8657-d636f5fcb54d" />

   *Figure 1 - Burp Suite HTTP history showing the POST /login request being sent to Intruder.*

2. Configured Burp Intruder for the username enumeration attack. In the "Positions" tab, cleared the default payload markers and set a single payload marker specifically around the `username` parameter's value (e.g., `username=§dummy§`). Left the password as a static value and ensured the attack type was set to "Sniper".
   
   <img width="1877" height="945" alt="image" src="https://github.com/user-attachments/assets/e742905e-41be-4240-b35c-4cbdd34c2952" />

   *Figure 2 - Burp Intruder Positions tab configured for a Sniper attack targeting the username parameter.*

3. In the "Payloads" tab, pasted the list of candidate usernames into the Simple list configuration. Clicked "Start attack". Once finished, clicked the "Length" column header to sort the results. Identified one request that had a different response length than the rest.
   
   <img width="918" height="599" alt="image" src="https://github.com/user-attachments/assets/f20d77c4-bab9-40c6-b138-0a2876906df9" />

   *Figure 3 - Burp Intruder attack results sorted by Length, highlighting the anomalous response.*

4. Compared the HTML response of the anomaly with the others. Observed that while most payloads returned an "Invalid username" error, the anomalous payload returned "Incorrect password", successfully confirming it as a valid registered username. Copied this enumerated username.
   
   <img width="532" height="363" alt="image" src="https://github.com/user-attachments/assets/064fcc45-820a-496a-8e75-335430959a60" />

   *Figure 4 - The HTTP response showing the "Incorrect password" error, confirming the username exists.*

5. Returned to the Intruder configuration to brute-force the password. Cleared the previous payload markers. Updated the `username` parameter to the valid username identified in Step 4. Placed a new payload marker around the `password` parameter's value (e.g., `password=§dummy§`).
   
   <img width="1859" height="830" alt="image" src="https://github.com/user-attachments/assets/590ea09f-b494-435f-ab8b-1e641d99e369" />

   *Figure 5 - Burp Intruder Positions tab reconfigured to target the password parameter using the enumerated username.*

6. In the "Payloads" tab, cleared the usernames list and pasted the list of candidate passwords. Clicked "Start attack". Monitored the "Status" column in the results table. Identified a single request that returned a `302 Found` redirect instead of a `200 OK`, indicating a successful login. Noted the winning password payload.
   
   <img width="943" height="731" alt="image" src="https://github.com/user-attachments/assets/2f3343ba-44b8-4496-8db1-6b18e9a22b1d" />

   *Figure 6 - Burp Intruder attack results showing the successful 302 Found redirect for the correct password payload.*

7. Returned to the web browser. Logged into the application using the enumerated username and the brute-forced password. The application granted access, successfully solving the lab.
   
   <img width="1902" height="794" alt="image" src="https://github.com/user-attachments/assets/62e58d44-3dd0-44c0-8835-bf72aeee02d1" />

   *Figure 7 - Successfully logging into the compromised account, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
* **Attack Type:** Burp Intruder (Sniper)
* **Target 1:** Username parameter (`username=§payload§`)
* **Target 2:** Password parameter (`password=§payload§`)

## 6. Mitigation / Remediation
To prevent username enumeration and brute-force attacks, authentication mechanisms must be hardened against automated guessing.
* **Generic Error Messages:** Ensure the application returns identical, generic error messages for both failed login states (e.g., "Invalid username or password"). Do not leak whether the username is valid or invalid.
* **Consistent Response Times:** Ensure that the backend processing time for valid and invalid usernames is practically identical so attackers cannot enumerate users via timing attacks.
* **Rate Limiting and Account Lockout:** Implement strict rate limiting on the `/login` endpoint to slow down automated attacks, and enforce temporary account lockouts after a certain number of failed consecutive attempts.
