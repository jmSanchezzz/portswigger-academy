# PortSwigger Lab: Reflected XSS into HTML Context with Nothing Encoded

## 1. Lab Information
**Title:** Lab: Reflected XSS into HTML context with nothing encoded
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Cross-Site Scripting (XSS)

## 2. Lab Objective
Perform a cross-site scripting attack using the search functionality that successfully calls the `alert` function.

## 3. Tools Used
* Web Browser

## 4. Step-by-Step Methodology

1. Accessed the lab environment and located the search bar on the main blog page.
   
   ![The main page of the application showing the search functionality](path/to/screenshot1.png)
   *Figure 1 - The main page of the application showing the search functionality.*

2. Tested the search feature by entering a standard text string (e.g., "test") to observe how the application handles and displays the input. Noticed that the search term is reflected directly onto the page (e.g., "0 search results for 'test'").
   
   ![The search results page showing the user input reflected directly in the HTML without encoding](path/to/screenshot2.png)
   *Figure 2 - The search results page showing the user input reflected directly in the HTML without encoding.*

3. To test if the application sanitizes HTML tags, entered the basic XSS payload `<script>alert(1)</script>` into the search box and clicked "Search".
   
   ![The XSS payload being entered into the search input field](path/to/screenshot3.png)
   *Figure 3 - The XSS payload being entered into the search input field.*

4. The application processed the search and reflected the payload back into the HTML document unmodified. The browser interpreted the injected `<script>` tags as executable JavaScript, triggering the alert box and solving the lab.
   
   ![The browser displaying the executed JavaScript alert pop-up box](path/to/screenshot4.png)
   *Figure 4 - The browser displaying the executed JavaScript alert pop-up box and the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```html
<script>alert(1)</script>