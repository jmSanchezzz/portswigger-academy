# Basic SSRF against the local server

## 1. Lab Information
**Title:** Lab: Basic SSRF against the local server  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Server-Side Request Forgery (SSRF)

## 2. Lab Objective
Exploit a Server-Side Request Forgery (SSRF) vulnerability in the application's stock check feature. The goal is to manipulate the backend request to access the internal administration panel hosted on `localhost` and delete the user `carlos`.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition

## 4. Step-by-Step Methodology

1. Accessed the lab environment and attempted to browse directly to the `/admin` path. Observed that the application blocked direct external access to the administration interface.
   
   <img width="1909" height="423" alt="image" src="https://github.com/user-attachments/assets/0256d115-f2a2-422b-a4b6-98d78413fee8" />

   *Figure 1 - The browser displaying an access denied message when attempting to visit the /admin path directly.*

2. Navigated to a product page and clicked the "Check stock" button. Switched to Burp Suite and located the resulting `POST /product/stock` request in the HTTP history. Sent this request to Burp Repeater. Observed that the application uses a `stockApi` parameter containing an encoded internal URL.
   
   <img width="1383" height="721" alt="image" src="https://github.com/user-attachments/assets/b9d02e4b-68b8-4607-b275-3d6447c8e42a" />

   *Figure 2 - Burp Suite HTTP history showing the POST request with the stockApi parameter.*

3. In Burp Repeater, modified the `stockApi` parameter to point to the local administration interface: `stockApi=http://localhost/admin`. Sent the request. The server bypassed its own external access controls, fetched the internal admin panel, and reflected the HTML in the response.
   
   

   <img width="1468" height="694" alt="image" src="https://github.com/user-attachments/assets/c70d354f-b134-40ef-8604-00f7fa078222" />

   *Figure 3 - Burp Repeater showing the modified stockApi parameter and the server's response containing the HTML of the internal admin panel.*

4. Analyzed the returned HTML code in the response panel to identify the specific functionality for deleting users. Located the target hyperlink: `http://localhost/admin/delete?username=carlos`.
   
   <img width="1476" height="435" alt="image" src="https://github.com/user-attachments/assets/a743df2c-add1-43cf-a035-f171eaf4bcab" />

   *Figure 4 - The Burp Repeater response panel highlighting the extracted deletion URL for the user carlos.*

5. Modified the `stockApi` parameter one final time to deliver the SSRF attack using the discovered endpoint: `stockApi=http://localhost/admin/delete?username=carlos`. Clicked "Send". The server executed the internal request, successfully deleting the user `carlos` and solving the lab.
   
   <img width="1471" height="701" alt="image" src="https://github.com/user-attachments/assets/a7ae372e-8bf9-479e-a7bc-a82ea6ed9009" />
   <img width="1904" height="256" alt="image" src="https://github.com/user-attachments/assets/e1fa59cd-6ac5-4b8d-ba3f-4fff925db362" />

   *Figure 5 - The HTTP request delivering the final SSRF payload, followed by the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```http
stockApi=http://localhost/admin/delete?username=carlos
