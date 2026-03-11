# Excessive trust in client-side controls

## 1. Lab Information
**Title:** Lab: Excessive trust in client-side controls  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Business Logic Vulnerabilities

## 2. Lab Objective
Exploit a logic flaw in the purchasing workflow where the application relies entirely on client-provided data for pricing. The goal is to intercept the "add to cart" request, manipulate the `price` parameter to an amount lower than the available store credit, and successfully purchase the "Lightweight l33t leather jacket".

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Proxy and Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and logged in using the provided credentials (`wiener:peter`). Navigated to the product page for the "Lightweight l33t leather jacket" and clicked "Add to cart". Attempted to checkout but was rejected due to insufficient store credit.
   
   <img width="1898" height="925" alt="image" src="https://github.com/user-attachments/assets/6aa109ca-7652-40c5-88a7-ed3133519b5f" />

   *Figure 1 - The shopping cart interface showing the order rejection due to insufficient funds.*

2. Switched to Burp Suite and navigated to **Proxy > HTTP history**. Located the `POST /cart` request that was generated when the jacket was added to the cart. Observed that the application insecurely transmits the item's `price` as a visible parameter in the request body. Sent this request to Burp Repeater.
   

   <img width="1871" height="942" alt="image" src="https://github.com/user-attachments/assets/3d4453ba-3327-4f1a-8042-6df7602165b7" />

   *Figure 2 - Burp Suite HTTP history showing the POST /cart request with the vulnerable price parameter.*

3. In Burp Repeater, modified the value of the `price` parameter from its original high cost to an arbitrary low integer (e.g., changing it to `1` or `100` cents). Clicked "Send" to add the manipulated item to the cart.
   
   <img width="1139" height="357" alt="image" src="https://github.com/user-attachments/assets/461b510b-ab3a-4a3d-9fee-2b4769fee5b4" />

   *Figure 3 - Burp Repeater showing the modified POST request with the injected low price.*

4. Returned to the web browser and navigated to the cart. Verified that the leather jacket was successfully added to the cart at the manipulated, significantly reduced price, well within the available store credit balance.
   
   <img width="1309" height="747" alt="image" src="https://github.com/user-attachments/assets/531c5c1c-bced-4d22-8683-5287943f0721" />

   *Figure 4 - The shopping cart reflecting the manipulated price of the leather jacket.*

5. Clicked the "Place order" button. The server processed the transaction using the manipulated price, granting the purchase and successfully solving the lab.
   
   <img width="1905" height="593" alt="image" src="https://github.com/user-attachments/assets/e05ecfb1-714a-4022-a348-73c4b87bf4ad" />

   *Figure 5 - The order confirmation screen, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
**Modified Request Body Parameter**
```http
price=1
```

## 6. Mitigation / Remediation
To prevent client-side control bypasses, applications must never trust the client to provide critical business data, such as pricing or privilege levels.
* **Server-Side Pricing:** The backend must independently determine the price of an item. When a user adds an item to their cart, the client should only send the `productId` and the `quantity`. The server must then look up the authoritative price for that specific `productId` directly from a secure backend database.
* **Validate All Input:** Treat all data originating from the client as untrusted. Implement strict server-side validation to ensure that any data modifying the state of the application aligns with the established business rules.
