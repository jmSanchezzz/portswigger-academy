# PortSwigger Lab: DOM XSS in document.write sink using source location.search

## 1. Lab Information
* **Title:** Lab: DOM XSS in document.write sink using source location.search
* **Difficulty Level:** Apprentice
* **Vulnerability Category:** DOM-based Cross-Site Scripting (DOM XSS)

## 2. Lab Objective
Perform a DOM-based cross-site scripting attack that calls the `alert` function by manipulating the `location.search` source, which is unsafely passed to the `document.write` sink.

## 3. Tools Used
* Web Browser (with Developer Tools / Inspector)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and entered a random alphanumeric string (e.g., "test1234") into the search box to trace how the application handles the input.
   
   <img src="path/to/screenshot1.png" alt="image" />

   *Figure 1 - Entering a random string into the search functionality to track the input.*

2. Right-clicked the page and selected "Inspect" to open the browser's Developer Tools. Searched the DOM for the injected string and observed that the JavaScript `document.write` function had placed the search query directly inside an `img src` attribute (e.g., `<img src="/resources/images/tracker.gif?searchTerms=test1234">`).
   
   <img src="path/to/screenshot2.png" alt="image" />

   *Figure 2 - Browser Developer Tools showing the input reflected inside the img tag's src attribute.*

3. Crafted a payload to break out of the existing `img` tag and inject a new element that executes JavaScript. Entered `"><svg onload=alert(1)>` into the search box and clicked "Search". (The `">` closes the `src` attribute and the `img` tag, while `<svg onload=alert(1)>` injects a scalable vector graphic that automatically fires the alert when it loads).
   
   <img src="path/to/screenshot3.png" alt="image" />

   *Figure 3 - The DOM XSS payload entered into the search input field.*

4. The application processed