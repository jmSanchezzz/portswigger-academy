# Basic SSRF against another back-end system

## 1. Lab Information
**Title:** Lab: Basic SSRF against another back-end system  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Server-Side Request Forgery (SSRF)

## 2. Lab Objective
Exploit a Server-Side Request Forgery (SSRF) vulnerability in the application's stock check feature. The goal is to use the stock check functionality to scan the internal `192.168.0.X` network range for an admin interface on port `8080`, and then use it to delete the user `carlos`.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Intruder and Repeater)

## 4. Step-by-Step Methodology

1. Accessed the lab environment, navigated to a product page, and clicked "Check stock". Switched to Burp Suite, located the resulting `POST /product/stock` request in the HTTP history, and sent it to Burp Intruder.
   
   <img width="1881" height="720" alt="image" src="https://github.com/user-attachments/assets/7b0b0940-86bc-4d85-9199-60683c16a084" />

   *Figure 1 - Burp Suite HTTP history showing the POST request being sent to Burp Intruder.*

2. In the Burp Intruder "Positions" tab, modified the `stockApi` parameter to target the internal network range on port 8080: `stockApi=http://192.168.0.1:8080/admin`. Highlighted the final octet (`1`) and clicked "Add §" to set it as the payload position.
   
   

   <img width="1881" height="504" alt="image" src="https://github.com/user-attachments/assets/1e699a3f-ad23-4015-8007-da8dac6ad641" />

   *Figure 2 - Burp Intruder Positions tab showing the payload marker placed on the final IP octet.*

3. In the "Payloads" tab, changed the payload type to "Numbers". Configured the payload to range From `1`, To `255`, with a Step of `1`. Clicked "Start attack".
   
   <img width="574" height="507" alt="image" src="https://github.com/user-attachments/assets/b4429de6-76af-488d-94ff-9c03d7e4c5d8" />

   *Figure 3 - Burp Intruder Payloads tab configured to iterate sequentially through the /24 subnet.*

4. Reviewed the Intruder attack results. Clicked the "Status" column to sort the results by HTTP status code. Identified a single IP address that returned a `200 OK` status, indicating the successful discovery of the internal admin interface.
   
   <img width="1885" height="950" alt="image" src="https://github.com/user-attachments/assets/d89c8dff-dae9-491d-b660-34f8db890ed2" />

   *Figure 4 - Intruder attack results showing the discovered internal IP address returning a 200 OK status.*

5. Sent the successful request from the Intruder results to Burp Repeater. Modified the `stockApi` parameter to execute the deletion functionality on the newly discovered IP address: `stockApi=http://192.168.0.[DISCOVERED_IP]:8080/admin/delete?username=carlos`. Clicked "Send". The server executed the internal request, successfully deleting the user `carlos` and solving the lab.
   
   <img width="1491" height="568" alt="image" src="https://github.com/user-attachments/assets/f72ba518-1ef2-433d-9c94-e5259f87bf90" />
   <img width="1904" height="255" alt="image" src="https://github.com/user-attachments/assets/83e2ac58-3010-44d9-9cb2-45d9e3e57207" />

   *Figure 5 - The HTTP request delivering the final SSRF payload to the discovered IP, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```http
stockApi=[http://192.168.0.](http://192.168.0.)X:8080/admin/delete?username=carlos
