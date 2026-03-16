# Accessing private GraphQL posts

## 1. Lab Information
**Title:** Lab: Accessing private GraphQL posts  
**Difficulty Level:** Apprentice  
**Vulnerability Category:** GraphQL API Vulnerabilities

## 2. Lab Objective
Exploit a GraphQL API that lacks proper access controls and leaves introspection enabled in a production environment. The goal is to identify a hidden blog post via sequential ID analysis, use an introspection query to discover an undocumented `postPassword` field, and execute a modified query to extract the secret password for the hidden post (ID 3).

## 3. Tools Used
* Web Browser
* Burp Suite Community Edition (Proxy, Repeater, and built-in GraphQL tools)

## 4. Step-by-Step Methodology

1. Accessed the lab environment and browsed the main blog page to populate the proxy history with normal traffic.
   
   <img width="1919" height="371" alt="Image" src="https://github.com/user-attachments/assets/1234ee6b-6ac0-4714-8e6a-fea0598feb76" />

   *Figure 1 - Browsing the main blog page to capture the initial API requests.*

2. Switched to Burp Suite and navigated to **Proxy > HTTP history**. Located the `POST /graphql/v1` request used by the application to retrieve the list of blog posts. Reviewed the JSON response and observed that the blog posts were assigned sequential IDs. Noticed that ID 3 was conspicuously missing from the sequence, indicating a hidden or unlisted post.
   
   <img width="746" height="748" alt="Image" src="https://github.com/user-attachments/assets/c95f0589-07b5-457b-88c1-2a1ba4c5124e" />

   *Figure 2 - Analyzing the GraphQL response and identifying the missing sequential ID (ID 3).*

3. To understand the structure of the API, right-clicked the `POST /graphql/v1` request and selected "Send to Repeater". In Repeater, right-clicked anywhere inside the Request panel and selected **GraphQL > Set introspection query**. Clicked "Send" to map the API's entire schema.
   
   <img width="1484" height="395" alt="Image" src="https://github.com/user-attachments/assets/526f3a60-1d95-4602-9f84-ef5c6aa7bcdc" />

   *Figure 3 - Sending an introspection query to the GraphQL endpoint to map the schema.*

4. Carefully reviewed the massive JSON response from the introspection query. Located the schema definition for the `BlogPost` type and discovered an undocumented, sensitive field named `postPassword` that is available to be queried.
   
   <img width="1511" height="571" alt="Image" src="https://github.com/user-attachments/assets/bd6309e2-11b2-42bf-a8e4-5389569a1bd8" />

   *Figure 4 - Discovering the undocumented postPassword field within the BlogPost schema.*

5. Returned to the HTTP history, located a standard `POST /graphql/v1` request used for fetching a single blog post, and sent it to a new Repeater tab.
   
   <img width="1497" height="700" alt="Image" src="https://github.com/user-attachments/assets/5592ad6c-c6ec-45a3-9fa9-31a7bd6229ad" />

   *Figure 5 - Sending a standard single-post GraphQL query to Repeater for modification.*

6. In the new Repeater tab, selected the dedicated GraphQL tab provided by Burp Suite. In the Variables panel, modified the `id` variable to `3` to target the hidden post. In the Query panel, added the newly discovered `postPassword` field to the requested data block alongside the standard fields. Clicked "Send".
   
   <img width="1494" height="586" alt="Image" src="https://github.com/user-attachments/assets/377647b4-af5f-4856-bd68-a8f998f5f232" />

   *Figure 6 - Modifying the GraphQL query to request the postPassword for the hidden post ID 3.*

7. The server processed the query and returned the details of the hidden blog post, including the secret password in the response body. Copied the exfiltrated password, navigated to the "Submit solution" dialog in the web browser, and submitted the secret to successfully solve the lab.
   
   <img width="1494" height="194" alt="Image" src="https://github.com/user-attachments/assets/1f6df7ea-6e17-4358-ae81-dac22b68d6f1" />
   <img width="1902" height="247" alt="Image" src="https://github.com/user-attachments/assets/9a5856e5-d8bb-4355-98de-9a897822b33c" />

   *Figure 7 - Extracting the secret password from the GraphQL response, followed by the lab completion banner.*

## 5. The Payload
**Modified GraphQL Query Variables & Fields**
> `Variables: {"id": 3}`
> `Query Addition: postPassword`

## 6. Mitigation / Remediation
To prevent information disclosure via GraphQL, applications must enforce strict access controls and minimize exposed surface area.
* **Disable Introspection in Production:** GraphQL introspection is a powerful development and debugging tool, but it essentially provides an attacker with a complete map of your API. It must be strictly disabled in all production environments.
* **Implement Object-Level and Field-Level Authorization:** Unlike REST APIs where authorization is often handled at the endpoint level, GraphQL requires granular authorization logic within the resolvers themselves. Ensure that authorization checks are performed before returning specific objects (like a hidden post) or specific fields (like a password), ensuring users can only query data they explicitly own or have permission to view.
