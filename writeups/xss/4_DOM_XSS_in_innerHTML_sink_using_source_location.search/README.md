# DOM XSS in innerHTML sink using source location.search

## 1. Lab Information
**Title:** Lab: DOM XSS in innerHTML sink using source location.search  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** DOM-based Cross-Site Scripting (DOM XSS)

## 2. Lab Objective
Perform a DOM-based cross-site scripting attack that calls the `alert` function by exploiting an `innerHTML` assignment that dynamically changes the HTML contents of a `div` element using untrusted data from `location.search`.

## 3. Tools Used
* Web Browser (with Developer Tools / Inspector)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and located the search functionality on the main blog page.
   
   <img width="1920" height="1027" alt="image" src="https://github.com/user-attachments/assets/4868e65b-0174-4538-b08c-c2f40d8fa981" />

   *Figure 1 - The main blog page showing the search functionality.*

2. Used the browser's Developer Tools to inspect the page's source code. Identified a vulnerable JavaScript block that retrieves the search query from the URL (`location.search`) and writes it directly to the page using the `innerHTML` property of a `div` element.
   
   <img width="1515" height="681" alt="image" src="https://github.com/user-attachments/assets/2df5bb4b-9f33-4afd-929c-066217c13a2d" />

   *Figure 2 - Browser Developer Tools showing the vulnerable JavaScript code mapping the URL parameter to the innerHTML sink.*

3. To exploit this behavior, crafted a payload using an HTML image tag with an intentionally broken source and an error handler: `<img src=1 onerror=alert(1)>`. Entered this payload into the search box and clicked "Search".
   
   <img width="1898" height="1026" alt="image" src="https://github.com/user-attachments/assets/ce27faa7-736a-471a-8842-c8fc5fd8200d" />

   *Figure 3 - The XSS payload being entered into the search input field.*

4. The application assigned the payload to the `innerHTML` of the `div`. The browser then attempted to load the image from the invalid source (`src=1`). Because it failed, it triggered the `onerror` event handler, which successfully executed the `alert(1)` JavaScript function and solved the lab.
   
   <img width="1919" height="917" alt="image" src="https://github.com/user-attachments/assets/e3a67e8b-3e19-4cab-ad7f-d3d3e1b4bb8f" />
   <img width="1898" height="1026" alt="image" src="https://github.com/user-attachments/assets/ef7b6e01-35e9-4103-becf-40aa13147eb3" />

   *Figure 4 - The browser displaying the executed JavaScript alert pop-up box and the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```html
<img src=1 onerror=alert(1)>
