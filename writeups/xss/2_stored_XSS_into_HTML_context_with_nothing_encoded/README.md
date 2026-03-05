# Stored XSS into HTML Context with Nothing Encoded

## 1. Lab Information
**Title:** Stored XSS into HTML context with nothing encoded
**Difficulty Level:** Apprentice
**Vulnerability Category:** Cross-Site Scripting (XSS)

## 2. Lab Objective
Submit a comment containing a cross-site scripting payload that calls the `alert` function when the blog post is viewed.

## 3. Tools Used
* Web Browser

## 4. Step-by-Step Methodology

1. Accessed the lab environment and navigated to a blog post to view the comment section.
   
   <img width="1902" height="1032" alt="image" src="https://github.com/user-attachments/assets/ca689e1f-6ca0-4623-aaff-36e73e55b554" />

   *Figure 1 - The blog post comment section.*

2. In the "Leave a comment" section, entered the XSS payload `<script>alert(1)</script>` into the "Comment" field. Filled out the required "Name", "Email", and "Website" fields with dummy data.
   
   <img width="1920" height="1030" alt="image" src="https://github.com/user-attachments/assets/4d547688-34f7-431e-b36f-2f828b7ecb01" />

   *Figure 2 - Filling out the comment form with the XSS payload.*

3. Clicked the "Post comment" button to submit the payload to the server's database.
   
   <img width="1901" height="1031" alt="image" src="https://github.com/user-attachments/assets/6ef28bb8-2984-422b-a80b-c5080f2b0e02" />

   *Figure 3 - The application confirming the comment was successfully posted.*

4. Navigated back to the blog post. The application loaded the stored comment from the database and reflected the payload directly into the HTML without encoding. The browser interpreted the injected `<script>` tags as executable JavaScript, triggering the alert box and solving the lab.
   
   <img width="1906" height="1029" alt="image" src="https://github.com/user-attachments/assets/8e84c975-52aa-49a0-ae63-0b6eb4e8a420" />

   *Figure 4 - The browser displaying the "Congratulations, you solved the lab!" banner.*

## 5. The Payload
```html
<script>alert(1)</script>
