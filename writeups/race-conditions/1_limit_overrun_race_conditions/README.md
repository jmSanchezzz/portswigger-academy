# Limit overrun race conditions

## 1. Lab Information
**Title:** Lab: Limit overrun race conditions  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Race Conditions / Business Logic

## 2. Lab Objective
Exploit a limit overrun race condition in the application's shopping cart mechanism. The goal is to bypass the business logic that restricts a discount code to a single use. By submitting multiple coupon application requests simultaneously, the objective is to stack the discount enough times to purchase the "Lightweight l33t leather jacket" using only the available store credit.

## 3. Tools Used
* Web Browser
* Burp Suite (Proxy - HTTP History and Repeater with Parallel Send / Single-packet attack)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and logged in using the provided credentials (`wiener:peter`). Located the provided discount code on the homepage. Added the target "Lightweight l33t leather jacket" to the shopping cart.
   
   <img width="1902" height="924" alt="Image" src="https://github.com/user-attachments/assets/d150b6cc-8e20-4054-bdb3-d374290e4bc9" />

   *Figure 1 - Adding the target leather jacket to the cart and identifying the available store credit.*

2. Applied the discount code normally to capture the workflow. Switched to Burp Suite and navigated to **Proxy > HTTP history**. Located the `POST /cart/coupon` request. Sent this request to Burp Repeater to prepare for the race condition attack.
   
   <img width="1500" height="450" alt="Image" src="https://github.com/user-attachments/assets/92938384-fe99-46b6-bea1-0321e7f252e9" />

   *Figure 2 - Isolating the POST /cart/coupon request in Burp HTTP history.*

3. In Burp Repeater, created a new Tab Group and added the `POST /cart/coupon` request to it. Duplicated the request tab 25 times within the same group to prepare a mass execution.
   
   <img width="1787" height="527" alt="Image" src="https://github.com/user-attachments/assets/8bdbae57-bfb1-474d-9b33-92da6b367836" />

   *Figure 3 - Duplicating the coupon application request into a dedicated Repeater group.*

4. Configured the Repeater group to use the "Send group in parallel" feature (which utilizes single-packet attacks in modern Burp Suite versions to minimize network jitter).
   
   <img width="1133" height="406" alt="Image" src="https://github.com/user-attachments/assets/98686d53-299f-41ba-b787-fcaa98c09147" />

   *Figure 4 - Configuring the Repeater tab group for parallel execution.*

5. Returned to the web browser and removed any previously applied coupons from the cart to ensure a clean state. Back in Burp Repeater, clicked "Send group (parallel)".
   
   <img width="1495" height="687" alt="Image" src="https://github.com/user-attachments/assets/5eb5dfc0-aced-4b17-8fbb-a0695ad267a2" />

   *Figure 5 - Executing the parallel requests. The responses indicate multiple successful applications before the database lock was enforced.*

6. Returned to the web browser and refreshed the shopping cart. Verified that the race condition was successful and the discount code had been applied multiple times, drastically reducing the total price. Clicked "Place order" to successfully purchase the jacket and solve the lab.
   
  <img width="1129" height="870" alt="Image" src="https://github.com/user-attachments/assets/bfc6a474-a661-41dc-bc44-b0cfb8aa956e" />
  <img width="1901" height="251" alt="Image" src="https://github.com/user-attachments/assets/9e357d22-1288-446d-b505-e901b9d53dbc" />

   *Figure 6 - The heavily discounted cart total and the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
**Parallel Request Execution (Single-Packet Attack)**
> `POST /cart/coupon HTTP/2`
> `Host: [LAB-ID].web-security-academy.net`
> `csrf=[TOKEN]&coupon=[DISCOUNT_CODE]`
> `*(Sent 25x simultaneously)*`

## 6. Mitigation / Remediation
To prevent limit overrun race conditions, applications must enforce strict data integrity and concurrency controls when processing state-changing actions.
* **Pessimistic Concurrency Control:** Implement database-level locking (e.g., `SELECT ... FOR UPDATE` in SQL) when querying a user's cart or coupon status. This prevents other concurrent threads from reading or modifying the same record until the current transaction is fully complete.
* **Atomic Operations:** Ensure that checking a limit (e.g., "has this coupon been applied?") and updating the database (e.g., "mark coupon as applied") occur as a single, indivisible atomic transaction.
* **Session/User Locks:** Implement application-level locking mechanisms that restrict a single user session to processing only one sensitive request at a time, forcing simultaneous requests to queue and execute sequentially.
