# PortSwigger Lab: Stored XSS into HTML Context with Nothing Encoded

## 1. Lab Information
* **Title:** Stored XSS into HTML context with nothing encoded
* **Difficulty Level:** Apprentice
* **Vulnerability Category:** Cross-Site Scripting (XSS)

## 2. Lab Objective
Submit a comment containing a cross-site scripting payload that calls the `alert` function when the blog post is viewed.

## 3. Tools Used
* Web Browser

## 4. Step-by-Step Methodology

1. Accessed the lab environment and navigated to a blog post to view the comment section.
   
   <img src="path/to/screenshot1.png" alt="image" />

   *Figure 1 - The blog post comment section.*

2. In the "Leave a comment" section, entered the XSS payload `<script>alert(1)</script>` into the "Comment" field. Filled out the required "Name", "Email", and "Website" fields with dummy data.
   
   <img src="path/to/screenshot2.png" alt="image" />

   *Figure 2 - Filling out the comment form with the XSS payload.*

3. Clicked the "Post comment" button to submit the payload to the server's database.
   
   <img src="path/to/screenshot3.png" alt="image" />

   *Figure 3 - The application confirming the comment was successfully posted.*

4. Navigated back to the blog post. The application loaded the stored comment from the database and reflected the payload directly into the HTML without encoding. The browser interpreted the injected `<script>` tags as executable JavaScript, triggering the alert box and solving the lab.
   
   <img src="path/to/screenshot4.png" alt="image" />

   *Figure 4 - The browser displaying the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```html
<script>alert(1)</script>