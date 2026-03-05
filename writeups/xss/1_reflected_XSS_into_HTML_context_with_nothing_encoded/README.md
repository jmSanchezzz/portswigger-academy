# Reflected XSS into HTML Context with Nothing Encoded

## 1. Lab Information
* **Title:** Lab: Reflected XSS into HTML context with nothing encoded
* **Difficulty Level:** Apprentice  
* **Vulnerability Category:** Cross-Site Scripting (XSS)

## 2. Lab Objective
Perform a cross-site scripting attack using the search functionality that successfully calls the `alert` function.

## 3. Tools Used
* Web Browser

## 4. Step-by-Step Methodology

1. Accessed the lab environment and located the search bar on the main blog page.
   
   <img width="1918" height="1042" alt="image" src="https://github.com/user-attachments/assets/7230adfd-b4c0-41da-89f5-7200b0cdf07d" />

   *Figure 1 - The main page of the application showing the search functionality.*

2. Tested the search feature by entering a standard text string (e.g., "test") to observe how the application handles and displays the input. Noticed that the search term is reflected directly onto the page (e.g., "0 search results for 'test'").
   
   <img width="1917" height="1027" alt="image" src="https://github.com/user-attachments/assets/b62f898c-aa45-4f85-a6f4-3c1e99e67298" />

   *Figure 2 - The search results page showing the user input reflected directly in the HTML without encoding.*

3. To test if the application sanitizes HTML tags, entered the basic XSS payload `<script>alert(1)</script>` into the search box and clicked "Search".
   
   <img width="1918" height="1026" alt="image" src="https://github.com/user-attachments/assets/885cc6d8-51a7-406d-b812-d8f44211baec" />
   <br>
   <img width="1915" height="1027" alt="image" src="https://github.com/user-attachments/assets/afa2f27d-4286-453c-93c6-66ef54f33e30" />

   *Figure 3 - The XSS payload being entered into the search input field.*

4. The application processed the search and reflected the payload back into the HTML document unmodified. The browser interpreted the injected `<script>` tags as executable JavaScript, triggering the alert box and solving the lab.
   
   <img width="1920" height="922" alt="image" src="https://github.com/user-attachments/assets/bdef42ab-0bfb-44b8-a201-7aab9e4c0df2" />

   *Figure 4 - The browser displaying the executed JavaScript alert pop-up box and the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```html
<script>alert(1)</script>
