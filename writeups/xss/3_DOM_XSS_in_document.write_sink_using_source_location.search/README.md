# DOM XSS in document.write sink using source location.search

## 1. Lab Information
**Title:** Lab: DOM XSS in document.write sink using source location.search  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** DOM-based Cross-Site Scripting (DOM XSS)

## 2. Lab Objective
Perform a DOM-based cross-site scripting attack that calls the `alert` function by manipulating the `location.search` source, which is unsafely passed to the `document.write` sink.

## 3. Tools Used
* Web Browser (with Developer Tools / Inspector)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and entered a random alphanumeric string (e.g., "test1234") into the search box to trace how the application handles the input.
   
   <img width="1901" height="1034" alt="image" src="https://github.com/user-attachments/assets/71f0f44e-451c-44cc-b333-72af4f6c92b1" />

   *Figure 1 - Entering a random string into the search functionality to track the input.*

2. Right-clicked the page and selected "Inspect" to open the browser's Developer Tools. Searched the DOM for the injected string and observed that the JavaScript `document.write` function had placed the search query directly inside an `img src` attribute (e.g., `<img src="/resources/images/tracker.gif?searchTerms=test1234">`).
   
   <img width="1508" height="645" alt="image" src="https://github.com/user-attachments/assets/b441fe14-a1b0-4d32-902b-0d38762f37da" />

   *Figure 2 - Browser Developer Tools showing the input reflected inside the img tag's src attribute.*

3. Crafted a payload to break out of the existing `img` tag and inject a new element that executes JavaScript. Entered `"><svg onload=alert(1)>` into the search box and clicked "Search". (The `">` closes the `src` attribute and the `img` tag, while `<svg onload=alert(1)>` injects a scalable vector graphic that automatically fires the alert when it loads).
   
   <img width="1920" height="1034" alt="image" src="https://github.com/user-attachments/assets/fbd0eae7-876d-4c2b-8dbc-4538b145924f" />

   *Figure 3 - The DOM XSS payload entered into the search input field.*

4. The application processed the URL parameter via JavaScript on the client side, broke out of the tag, and immediately executed the injected alert function, solving the lab.
   
   <img width="1920" height="1032" alt="image" src="https://github.com/user-attachments/assets/00a3f527-12f2-46c8-aa32-d8d45f6381b9" />
   <img width="1920" height="1032" alt="image" src="https://github.com/user-attachments/assets/52df5c68-f31a-4156-8e0d-c46b01e8035b" />
   
   *Figure 4 - The browser displaying the executed JavaScript alert pop-up box and the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```html
"><svg onload=alert(1)>
