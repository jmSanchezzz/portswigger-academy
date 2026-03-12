# Flawed enforcement of business rules

## 1. Lab Information
**Title:** Lab: Flawed enforcement of business rules  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Business Logic Vulnerabilities

## 2. Lab Objective
Exploit a business logic flaw in the application's checkout workflow where coupon code restrictions are inadequately enforced. The goal is to obtain two valid coupon codes and alternate their application to bypass the reuse restriction, stacking discounts until the "Lightweight l33t leather jacket" can be purchased with the limited available store credit.

## 3. Tools Used
* Web Browser

## 4. Step-by-Step Methodology

1. Accessed the lab environment and logged in using the provided credentials (`wiener:peter`). On the home page, identified a visible coupon code: `NEWCUST5`. Scrolled to the bottom of the page, entered an arbitrary email into the newsletter signup form, and received a second coupon code: `SIGNUP30`.
   
   <img width="1905" height="373" alt="image" src="https://github.com/user-attachments/assets/6a0a86e9-7c29-4de2-ab14-15e1c14dad1f" />
   <img width="558" height="213" alt="image" src="https://github.com/user-attachments/assets/fd96e359-6609-475b-aa33-c886e16aef7a" />

   *Figure 1 - Obtaining the two valid coupon codes: NEWCUST5 and SIGNUP30.*

2. Navigated to the product page for the target "Lightweight l33t leather jacket" and clicked "Add to cart". Navigated to the shopping cart to begin the checkout process.
   
   <img width="968" height="320" alt="image" src="https://github.com/user-attachments/assets/8f80a94f-3a43-4ade-8cf7-e2bcc5a63505" />

   *Figure 2 - Adding the target leather jacket to the shopping cart.*

3. In the shopping cart, applied the `NEWCUST5` coupon, then applied the `SIGNUP30` coupon. Both applied successfully. Attempted to apply `SIGNUP30` a second time in a row and received a "Coupon already applied" error.
   
   <img width="1010" height="459" alt="image" src="https://github.com/user-attachments/assets/28d00d15-3db1-4adc-beb7-48eadb912c19" />

   *Figure 3 - The application rejecting the back-to-back submission of the same coupon code.*

4. To test the robustness of this restriction, alternated the input and applied the `NEWCUST5` code again. The system accepted it, revealing that the validation logic only checks the most recently applied coupon rather than the entire history of the cart.
   
   <img width="438" height="256" alt="image" src="https://github.com/user-attachments/assets/e9e75344-a420-43a0-9060-5c886ac5d6a5" />
   *Figure 4 - Successfully bypassing the restriction by alternating the coupon codes.*

5. Continued to alternate applying the `NEWCUST5` and `SIGNUP30` codes repeatedly. Exploited this logic flaw to stack the discounts until the total price of the leather jacket was reduced to an amount lower than the available store credit balance.
   
  
   <img width="638" height="453" alt="image" src="https://github.com/user-attachments/assets/60128fed-650a-4eb7-87da-a21ed82d6e8e" />

   *Figure 5 - The heavily discounted shopping cart total after repeatedly stacking the alternating coupons.*

6. Clicked the "Place order" button. The server processed the manipulated cart total, granting the purchase and successfully solving the lab.
   
   <img width="1894" height="473" alt="image" src="https://github.com/user-attachments/assets/e0633d42-6322-489f-b28c-60925e3db017" />

   *Figure 6 - The order confirmation screen, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
**Alternating Coupon Codes**
> `NEWCUST5`
> `SIGNUP30`

## 6. Mitigation / Remediation
To prevent coupon stacking and business rule bypasses, applications must track the comprehensive state of a transaction on the server side.
* **Maintain Cart History:** The backend application must maintain a persistent record (e.g., in a database table or secure server-side session) of every coupon code applied to a specific cart or order ID.
* **Comprehensive Validation:** When a user attempts to apply a discount, the validation logic must check the submitted code against the entire list of previously applied codes for that order, not just the single most recent entry.
* **Strict Stacking Limits:** Implement global configuration rules that dictate how many promotional codes can be applied to a single order (e.g., limiting carts to a maximum of one active promotional code at a time).
