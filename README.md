# PortSwigger Web Security Academy - Lab Tracker

[![Overall Progress](https://img.shields.io/badge/Progress-14%2F251%20Labs-red?style=for-the-badge&logo=target)](https://portswigger.net/web-security)
[![Burp Suite](https://img.shields.io/badge/Tools-BurpSuite%20%7C%20OWASP-orange?style=for-the-badge)](https://portswigger.net/burp)
[![Status](https://img.shields.io/badge/Status-Initializing...-lightgrey?style=for-the-badge)]()

A systematic roadmap to mastering web application security. This repository tracks my hands-on journey through the PortSwigger Academy, documenting every vulnerability pwned and every technique learned.

---

## Progress Dashboard

| Vulnerability Category | Completed | Status |
| :--- | :---: | :--- |
| [1. SQL Injection](#1-sql-injection-18-labs) | 2 / 18 | In Progress|
| [2. Cross-Site Scripting (XSS)](#2-cross-site-scripting-30-labs) | 9 / 30 | In Progress|
| [3. CSRF](#3-cross-site-request-forgery-12-labs) | 1 / 12 | In Progress|
| [4. Clickjacking](#4-clickjacking-5-labs) | 2 / 5 | In Progress|
| [5. DOM-based vulnerabilities](#5-dom-based-vulnerabilities-7-labs) | 0 / 7 | Not Started|
| [6. CORS](#6-cross-origin-resource-sharing-cors-3-labs) | 0 / 3 | Not Started|
| [7. XXE Injection](#7-xml-external-entity-xxe-injection-9-labs) | 0 / 9 | Not Started|
| [8. SSRF](#8-server-side-request-forgery-ssrf-7-labs) | 0 / 7 | Not Started|
| [9. HTTP request smuggling](#9-http-request-smuggling-21-labs) | 0 / 21 | Not Started |
| [10. OS command injection](#10-os-command-injection-5-labs) | 0 / 5 | Not Started |
| [11. Server-side template injection](#11-server-side-template-injection-7-labs) | 0 / 7 | Not Started |
| [12. Path traversal](#12-path-traversal-6-labs) | 0 / 6 | Not Started |
| [13. Access control vulnerabilities](#13-access-control-vulnerabilities-13-labs) | 0 / 13 | Not Started |
| [14. Authentication](#14-authentication-14-labs) | 0 / 14 | Not Started |
| [15. WebSockets](#15-websockets-3-labs) | 0 / 3 | Not Started |
| [16. Web cache poisoning](#16-web-cache-poisoning-13-labs) | 0 / 13 | Not Started |
| [17. Insecure deserialization](#17-insecure-deserialization-10-labs) | 0 / 10 | Not Started |
| [18. Information disclosure](#18-information-disclosure-5-labs) | 0 / 5 | Not Started |
| [19. Business logic vulnerabilities](#19-business-logic-vulnerabilities-11-labs) | 0 / 11 | Not Started |
| [20. HTTP Host header attacks](#20-http-host-header-attacks-7-labs) | 0 / 7 | Not Started |
| [21. OAuth authentication](#21-oauth-authentication-6-labs) | 0 / 6 | Not Started |
| [22. File upload vulnerabilities](#22-file-upload-vulnerabilities-7-labs) | 0 / 7 | Not Started |
| [23. JWT](#23-jwt-8-labs) | 0 / 8 | Not Started |
| [24. Essential skills](#24-essential-skills-2-labs) | 0 / 2 | Not Started |
| [25. Prototype pollution](#25-prototype-pollution-10-labs) | 0 / 10 | Not Started |
| [26. GraphQL API vulnerabilities](#26-graphql-api-vulnerabilities-5-labs) | 0 / 5 | Not Started |
| [27. Race conditions](#27-race-conditions-6-labs) | 0 / 6 | Not Started |
| [28. NoSQL injection](#28-nosql-injection-4-labs) | 0 / 4 | Not Started |
| [29. API testing](#29-api-testing-5-labs) | 0 / 5 | Not Started |
| [30. Web LLM attacks](#30-web-llm-attacks-4-labs) | 0 / 4 | Not Started |
| [31. Web cache deception](#31-web-cache-deception-5-labs) | 0 / 5 | Not Started |
| **Total Academy Progress** | **14 / 251** | **5%** |
---

## Vulnerability List & Lab Tracker

<details>
<summary><b>1. SQL Injection (18 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | SQL injection in WHERE clause | ✅ Pwned | [📝](./writeups/sql-injection/1_SQL_injection_vulnerability_in_WHERE_clause_allowing_retrieval_of_hidden_data/README.md) |
| Apprentice | SQLi allowing login bypass | ✅ Pwned | [📝](./writeups/sql-injection/2_SQL_Injection_vulnerability_allowing_login_bypass/README.md) |
| Practitioner | SQLi querying DB type/version (Oracle) | ⬜ Not Pwned | [📝](#) |
| Practitioner | SQLi querying DB type/version (MySQL/MS) | ⬜ Not Pwned | [📝](#) |
| Practitioner | SQLi listing DB contents (non-Oracle) | ⬜ Not Pwned | [📝](#) |
| Practitioner | SQLi listing DB contents (Oracle) | ⬜ Not Pwned | [📝](#) |
| Practitioner | SQLi UNION attack (Column count) | ⬜ Not Pwned | [📝](#) |
| Practitioner | SQLi UNION attack (Finding text columns) | ⬜ Not Pwned | [📝](#) |
| Practitioner | SQLi UNION attack (Data from other tables) | ⬜ Not Pwned | [📝](#) |
| Practitioner | SQLi UNION attack (Multiple values) | ⬜ Not Pwned | [📝](#) |
| Practitioner | Blind SQLi (Conditional responses) | ⬜ Not Pwned | [📝](#) |
| Practitioner | Blind SQLi (Conditional errors) | ⬜ Not Pwned | [📝](#) |
| Practitioner | Visible error-based SQLi | ⬜ Not Pwned | [📝](#) |
| Practitioner | Blind SQLi (Time delays) | ⬜ Not Pwned | [📝](#) |
| Practitioner | Blind SQLi (Time delays + Info retrieval) | ⬜ Not Pwned | [📝](#) |
| Practitioner | Blind SQLi (Out-of-band interaction) | ⬜ Not Pwned | [📝](#) |
| Practitioner | Blind SQLi (Out-of-band exfiltration) | ⬜ Not Pwned | [📝](#) |
| Practitioner | SQLi with filter bypass via XML encoding | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>2. Cross-Site Scripting (XSS) (30 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Reflected XSS into HTML context with nothing encoded | ✅ Pwned | [📝](./writeups/xss/1_reflected_XSS_into_HTML_context_with_nothing_encoded/README.md) |
| Apprentice | Stored XSS into HTML context with nothing encoded | ✅ Pwned | [📝](./writeups/xss/2_stored_XSS_into_HTML_context_with_nothing_encoded/README.md) |
| Apprentice | DOM XSS in `document.write` sink using source `location.search` | ✅ Pwned | [📝](./writeups/xss/3_DOM_XSS_in_document.write_sink_using_source_location.search/README.md) |
| Apprentice | DOM XSS in `innerHTML` sink using source `location.search` | ✅ Pwned | [📝](./writeups/xss/4_DOM_XSS_in_innerHTML_sink_using_source_location.search/README.md) |
| Apprentice | DOM XSS in jQuery anchor `href` attribute sink using `location.search` source |  ✅ Pwned | [📝](./writeups/xss/5_DOM_XSS_in_jQuery_anchor_href_attribute_sink_using_location.search_source/README.md) |
| Apprentice | DOM XSS in jQuery selector sink using a hashchange event |✅ Pwned | [📝](./writeups/xss/6_DOM_XSS_in_jQuery_selector_sink_using_a_hashchange_event/README.md) |
| Apprentice | Reflected XSS into attribute with angle brackets HTML-encoded |✅ Pwned | [📝](./writeups/xss/7_Reflected_XSS_into_attribute_with_angle_brackets_HTML-encoded/README.md) |
| Apprentice | Stored XSS into anchor `href` attribute with double quotes HTML-encoded | ✅ Pwned | [📝](./writeups/xss/8_stored_XSS_into_anchor_href_attribute_with_double_quotes_HTML-encoded/README.md) |
| Apprentice | Reflected XSS into a JavaScript string with angle brackets HTML encoded | ✅ Pwned | [📝](./writeups/xss/8_reflected_XSS_into_a_JavaScript_string_with_angle_brackets_HTML_encoded/README.md) |
| Practitioner | DOM XSS in `document.write` sink using source `location.search` inside a select element | ⬜ Not Pwned | [📝](#) |
| Practitioner | DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded | ⬜ Not Pwned | [📝](#) |
| Practitioner | Reflected DOM XSS | ⬜ Not Pwned | [📝](#) |
| Practitioner | Stored DOM XSS | ⬜ Not Pwned | [📝](#) |
| Practitioner | Reflected XSS into HTML context with most tags and attributes blocked | ⬜ Not Pwned | [📝](#) |
| Practitioner | Reflected XSS into HTML context with all tags blocked except custom ones | ⬜ Not Pwned | [📝](#) |
| Practitioner | Reflected XSS with some SVG markup allowed | ⬜ Not Pwned | [📝](#) |
| Practitioner | Reflected XSS in canonical link tag | ⬜ Not Pwned | [📝](#) |
| Practitioner | Reflected XSS into a JavaScript string with single quote and backslash escaped | ⬜ Not Pwned | [📝](#) |
| Practitioner | Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped | ⬜ Not Pwned | [📝](#) |
| Practitioner | Stored XSS into `onclick` event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped | ⬜ Not Pwned | [📝](#) |
| Practitioner | Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting cross-site scripting to steal cookies | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting cross-site scripting to capture passwords | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting XSS to bypass CSRF defenses | ⬜ Not Pwned | [📝](#) |
| Practitioner | Reflected XSS protected by very strict CSP, with dangling markup attack | ⬜ Not Pwned | [📝](#) |
| Expert | Reflected XSS with AngularJS sandbox escape without strings | ⬜ Not Pwned | [📝](#) |
| Expert | Reflected XSS with AngularJS sandbox escape and CSP | ⬜ Not Pwned | [📝](#) |
| Expert | Reflected XSS with event handlers and `href` attributes blocked | ⬜ Not Pwned | [📝](#) |
| Expert | Reflected XSS in a JavaScript URL with some characters blocked | ⬜ Not Pwned | [📝](#) |
| Expert | Reflected XSS protected by CSP, with CSP bypass | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>3. Cross-Site Request Forgery (CSRF) (12 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | CSRF with no defenses | ✅ Pwned | [📝](./writeups/csrf/1_CSRF_vulnerability_with_no_defenses/README.md) |
| Practitioner | CSRF (Token validation depends on method) | ⬜ Not Pwned | [📝](#) |
| Practitioner | CSRF (Token not tied to session) | ⬜ Not Pwned | [📝](#) |
| Practitioner | CSRF where token is tied to non-session cookie | ⬜ Not Pwned | [📝](#) |
| Practitioner | CSRF where token is duplicated in cookie | ⬜ Not Pwned | [📝](#) |
| Practitioner | SameSite Lax bypass via method override | ⬜ Not Pwned | [📝](#) |
| Practitioner | SameSite Strict bypass via client-side redirect | ⬜ Not Pwned | [📝](#) |
| Practitioner | SameSite Strict bypass via sibling domain | ⬜ Not Pwned | [📝](#) |
| Practitioner | SameSite Lax bypass via cookie refresh | ⬜ Not Pwned | [📝](#) |
| Practitioner | CSRF where Referer validation depends on header being present | ⬜ Not Pwned | [📝](#) |
| Practitioner | CSRF with broken Referer validation | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>4. Clickjacking (5 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Basic clickjacking with CSRF token protection | ✅ Pwned | [📝](./writeups/clickjacking/1_basic_clickjacking_with_CSRF_token_protection/README.md) |
| Apprentice | Clickjacking with form input data prefilled from a URL parameter | ✅ Pwned | [📝](./writeups/clickjacking/2_clickjacking_with_form_input_data_prefilled_from_a_URL_parameter/README.md) |
| Apprentice | Clickjacking with a frame buster script | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting clickjacking vulnerability to trigger DOM-based XSS | ⬜ Not Pwned | [📝](#) |
| Practitioner | Multistep clickjacking | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>5. DOM-based vulnerabilities (7 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Practitioner | DOM XSS using web messages | ⬜ Not Pwned | [📝](#) |
| Practitioner | DOM XSS using web messages and a JavaScript URL | ⬜ Not Pwned | [📝](#) |
| Practitioner | DOM XSS using web messages and JSON.parse | ⬜ Not Pwned | [📝](#) |
| Practitioner | DOM-based open redirection | ⬜ Not Pwned | [📝](#) |
| Practitioner | DOM-based cookie manipulation | ⬜ Not Pwned | [📝](#) |
| Expert | Exploiting DOM clobbering to enable XSS | ⬜ Not Pwned | [📝](#) |
| Expert | Clobbering DOM attributes to bypass HTML filters | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>6. Cross-origin resource sharing (CORS) (3 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | CORS vulnerability with basic origin reflection | ⬜ Not Pwned | [📝](#) |
| Apprentice | CORS vulnerability with trusted null origin | ⬜ Not Pwned | [📝](#) |
| Practitioner | CORS vulnerability with trusted insecure protocols | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>7. XML external entity (XXE) injection (9 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Exploiting XXE using external entities to retrieve files | ⬜ Not Pwned | [📝](#) |
| Apprentice | Exploiting XXE to perform SSRF attacks | ⬜ Not Pwned | [📝](#) |
| Practitioner | Blind XXE with out-of-band interaction | ⬜ Not Pwned | [📝](#) |
| Practitioner | Blind XXE with out-of-band interaction via XML parameter entities | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting blind XXE to exfiltrate data using a malicious external DTD | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting blind XXE to retrieve data via error messages | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting XInclude to retrieve files | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting XXE via image file upload | ⬜ Not Pwned | [📝](#) |
| Expert | Exploiting XXE to retrieve data by repurposing a local DTD | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>8. Server-side request forgery (SSRF) (7 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Basic SSRF against the local server | ⬜ Not Pwned | [📝](#) |
| Apprentice | Basic SSRF against another back-end system | ⬜ Not Pwned | [📝](#) |
| Practitioner | Blind SSRF with out-of-band detection | ⬜ Not Pwned | [📝](#) |
| Practitioner | SSRF with blacklist-based input filter | ⬜ Not Pwned | [📝](#) |
| Practitioner | SSRF with filter bypass via open redirection vulnerability | ⬜ Not Pwned | [📝](#) |
| Expert | Blind SSRF with Shellshock exploitation | ⬜ Not Pwned | [📝](#) |
| Expert | SSRF with whitelist-based input filter | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>9. HTTP request smuggling (21 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Practitioner | HTTP request smuggling, confirming a CL.TE vulnerability via differential responses | ⬜ Not Pwned | [📝](#) |
| Practitioner | HTTP request smuggling, confirming a TE.CL vulnerability via differential responses | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting HTTP request smuggling to bypass front-end security controls, CL.TE vulnerability | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting HTTP request smuggling to bypass front-end security controls, TE.CL vulnerability | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting HTTP request smuggling to reveal front-end request rewriting | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting HTTP request smuggling to capture other users' requests | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting HTTP request smuggling to deliver reflected XSS | ⬜ Not Pwn
