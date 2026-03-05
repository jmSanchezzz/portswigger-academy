# Stored XSS into anchor href attribute with double quotes HTML-encoded

## 1. Lab Information
**Title:** Lab: Stored XSS into anchor href attribute with double quotes HTML-encoded  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** Stored Cross-Site Scripting (XSS)

## 2. Lab Objective
Exploit a stored XSS vulnerability in the comment functionality by submitting a payload in the "Website" field that calls the `alert` function when the comment author's name is clicked.

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition

## 4. Step-by-Step Methodology

1. Accessed the lab environment, navigated to a blog post, and submitted a test comment. Entered a random alphanumeric string (e.g., `http://test1234.com`) into the "Website" input field to trace how the application stores and renders the data.
   

   <img width="1152" height="836" alt="image" src="https://github.com/user-attachments/assets/ecd3f336-c1be-45ac-875f-2907c6e58c80" />

   *Figure 1 - The blog comment form filled out with a test string in the Website field.*

2. Used Burp Suite to intercept the `POST` request for the comment submission, as well as the subsequent `GET` request to view the loaded comment on the blog post. Sent the `GET` request to Burp Repeater.
   
   <img width="1386" height="428" alt="image" src="https://github.com/user-attachments/assets/54fc4b97-5b3d-4a25-a209-d148416bd9c2" />

   *Figure 2 - Burp Suite Repeater showing the GET request and the HTTP response.*

3. Analyzed the HTTP response in Burp Repeater. Observed that the random string from the "Website" field was reflected directly inside the `href` attribute of the anchor (`<a>`) tag surrounding the comment author's name. Because double quotes were safely HTML-encoded, breaking out of the attribute wasn't possible. Instead, a new comment was submitted using a JavaScript pseudo-protocol as the payload in the Website field: `javascript:alert(1)`.
   
   <img width="1130" height="871" alt="image" src="https://github.com/user-attachments/assets/9ede0808-06d2-4703-9634-0b80bb649537" />

   *Figure 3 - Submitting a new comment with the JavaScript pseudo-protocol payload in the Website field.*

4. Navigated back to the blog post to view the newly posted comment. Clicked on the author's name above the comment. Because the `href` attribute contained `javascript:alert(1)`, the browser executed the code instead of navigating to a URL, triggering the alert box and solving the lab.
   
   <img width="1899" height="253" alt="image" src="https://github.com/user-attachments/assets/69b25486-a249-459d-a6c5-377bfb118d6f" />

   *Figure 4 - The browser displaying the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```javascript
javascript:alert(1)
