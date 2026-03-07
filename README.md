# PortSwigger Web Security Academy - Lab Tracker

[![Overall Progress](https://img.shields.io/badge/Progress-18%2F251%20Labs-red?style=for-the-badge&logo=target)](https://portswigger.net/web-security)
[![Burp Suite](https://img.shields.io/badge/Tools-BurpSuite%20%7C%20OWASP-orange?style=for-the-badge)](https://portswigger.net/burp)
[![Status](https://img.shields.io/badge/Status-Initializing...-lightgrey?style=for-the-badge)]()

A systematic roadmap to mastering web application security. This repository tracks my hands-on journey through the PortSwigger Academy, documenting every vulnerability pwned and every technique learned.

---

## Progress Dashboard

| Vulnerability Category | Completed | Status |
| :--- | :---: | :--- |
| [1. SQL Injection](#1-sql-injection-18-labs) | 2 / 18 | In Progress |
| [2. Cross-Site Scripting (XSS)](#2-cross-site-scripting-xss-30-labs) | 9 / 30 | In Progress |
| [3. CSRF](#3-csrf-12-labs) | 1 / 12 | In Progress |
| [4. Clickjacking](#4-clickjacking-5-labs) | 3 / 5 | In Progress |
| [5. DOM-based vulnerabilities](#5-dom-based-vulnerabilities-7-labs) | 0 / 7 | Not Started |
| [6. CORS](#6-cors-3-labs) | 2 / 3 | In Progress |
| [7. XXE Injection](#7-xxe-injection-9-labs) | 1 / 9 | In Progress |
| [8. SSRF](#8-ssrf-7-labs) | 0 / 7 | Not Started |
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
| **Total Academy Progress** | **18 / 251** | **7%** |

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
| Apprentice | Clickjacking with a frame buster script | ✅ Pwned | [📝](./writeups/clickjacking/3_clickjacking_with_a_frame_buster_script/README.md) |
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
| Apprentice | CORS vulnerability with basic origin reflection | ✅ Pwned | [📝](./writeups/cors/1_CORS_vulnerability_with_basic_origin_reflection/README.md) |
| Apprentice | CORS vulnerability with trusted null origin | ✅ Pwned | [📝](./writeups/cors/2_CORS_vulnerability_with_trusted_null_origin/README.md) |
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
| Practitioner | Exploiting HTTP request smuggling to deliver reflected XSS | ⬜ Not Pwned | [📝](#) |
| Practitioner | Response queue poisoning via H2.TE request smuggling | ⬜ Not Pwned | [📝](#) |
| Practitioner | H2.CL request smuggling | ⬜ Not Pwned | [📝](#) |
| Practitioner | HTTP/2 request smuggling via CRLF injection | ⬜ Not Pwned | [📝](#) |
| Practitioner | HTTP/2 request splitting via CRLF injection | ⬜ Not Pwned | [📝](#) |
| Expert | 0.CL request smuggling | ⬜ Not Pwned | [📝](#) |
| Practitioner | CL.0 request smuggling | ⬜ Not Pwned | [📝](#) |
| Practitioner | HTTP request smuggling, basic CL.TE vulnerability | ⬜ Not Pwned | [📝](#) |
| Practitioner | HTTP request smuggling, basic TE.CL vulnerability | ⬜ Not Pwned | [📝](#) |
| Practitioner | HTTP request smuggling, obfuscating the TE header | ⬜ Not Pwned | [📝](#) |
| Expert | Exploiting HTTP request smuggling to perform web cache poisoning | ⬜ Not Pwned | [📝](#) |
| Expert | Exploiting HTTP request smuggling to perform web cache deception | ⬜ Not Pwned | [📝](#) |
| Expert | Bypassing access controls via HTTP/2 request tunnelling | ⬜ Not Pwned | [📝](#) |
| Expert | Web cache poisoning via HTTP/2 request tunnelling | ⬜ Not Pwned | [📝](#) |
| Expert | Client-side desync | ⬜ Not Pwned | [📝](#) |
| Expert | Server-side pause-based request smuggling | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>10. OS command injection (5 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | OS command injection, simple case | ⬜ Not Pwned | [📝](#) |
| Practitioner | Blind OS command injection with time delays | ⬜ Not Pwned | [📝](#) |
| Practitioner | Blind OS command injection with output redirection | ⬜ Not Pwned | [📝](#) |
| Practitioner | Blind OS command injection with out-of-band interaction | ⬜ Not Pwned | [📝](#) |
| Practitioner | Blind OS command injection with out-of-band data exfiltration | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>11. Server-side template injection (7 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Practitioner | Basic server-side template injection | ⬜ Not Pwned | [📝](#) |
| Practitioner | Basic server-side template injection (code context) | ⬜ Not Pwned | [📝](#) |
| Practitioner | Server-side template injection using documentation | ⬜ Not Pwned | [📝](#) |
| Practitioner | Server-side template injection in an unknown language with a documented exploit | ⬜ Not Pwned | [📝](#) |
| Practitioner | Server-side template injection with information disclosure via user-supplied objects | ⬜ Not Pwned | [📝](#) |
| Expert | Server-side template injection in a sandboxed environment | ⬜ Not Pwned | [📝](#) |
| Expert | Server-side template injection with a custom exploit | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>12. Path traversal (6 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | File path traversal, simple case | ⬜ Not Pwned | [📝](#) |
| Practitioner | File path traversal, traversal sequences blocked with absolute path bypass | ⬜ Not Pwned | [📝](#) |
| Practitioner | File path traversal, traversal sequences stripped non-recursively | ⬜ Not Pwned | [📝](#) |
| Practitioner | File path traversal, traversal sequences stripped with superfluous URL-decode | ⬜ Not Pwned | [📝](#) |
| Practitioner | File path traversal, validation of start of path | ⬜ Not Pwned | [📝](#) |
| Practitioner | File path traversal, validation of file extension with null byte bypass | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>13. Access control vulnerabilities (13 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Unprotected admin functionality | ⬜ Not Pwned | [📝](#) |
| Apprentice | Unprotected admin functionality with unpredictable URL | ⬜ Not Pwned | [📝](#) |
| Apprentice | User role controlled by request parameter | ⬜ Not Pwned | [📝](#) |
| Apprentice | User role can be modified in user profile | ⬜ Not Pwned | [📝](#) |
| Apprentice | User ID controlled by request parameter | ⬜ Not Pwned | [📝](#) |
| Apprentice | User ID controlled by request parameter, with unpredictable user IDs | ⬜ Not Pwned | [📝](#) |
| Apprentice | User ID controlled by request parameter with data leakage in redirect | ⬜ Not Pwned | [📝](#) |
| Apprentice | User ID controlled by request parameter with password disclosure | ⬜ Not Pwned | [📝](#) |
| Apprentice | Insecure direct object references | ⬜ Not Pwned | [📝](#) |
| Practitioner | URL-based access control can be circumvented | ⬜ Not Pwned | [📝](#) |
| Practitioner | Method-based access control can be circumvented | ⬜ Not Pwned | [📝](#) |
| Practitioner | Multi-step process with no access control on one step | ⬜ Not Pwned | [📝](#) |
| Practitioner | Referer-based access control | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>14. Authentication (14 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Username enumeration via different responses | ⬜ Not Pwned | [📝](#) |
| Apprentice | 2FA simple bypass | ⬜ Not Pwned | [📝](#) |
| Apprentice | Password reset broken logic | ⬜ Not Pwned | [📝](#) |
| Practitioner | Username enumeration via subtly different responses | ⬜ Not Pwned | [📝](#) |
| Practitioner | Username enumeration via response timing | ⬜ Not Pwned | [📝](#) |
| Practitioner | Broken brute-force protection, IP block | ⬜ Not Pwned | [📝](#) |
| Practitioner | Username enumeration via account lock | ⬜ Not Pwned | [📝](#) |
| Practitioner | 2FA broken logic | ⬜ Not Pwned | [📝](#) |
| Practitioner | Brute-forcing a stay-logged-in cookie | ⬜ Not Pwned | [📝](#) |
| Practitioner | Offline password cracking | ⬜ Not Pwned | [📝](#) |
| Practitioner | Password reset poisoning via middleware | ⬜ Not Pwned | [📝](#) |
| Practitioner | Password brute-force via password change | ⬜ Not Pwned | [📝](#) |
| Expert | Broken brute-force protection, multiple credentials per request | ⬜ Not Pwned | [📝](#) |
| Expert | 2FA bypass using a brute-force attack | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>15. WebSockets (3 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Manipulating WebSocket messages to exploit vulnerabilities | ⬜ Not Pwned | [📝](#) |
| Practitioner | Cross-site WebSocket hijacking | ⬜ Not Pwned | [📝](#) |
| Practitioner | Manipulating the WebSocket handshake to exploit vulnerabilities | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>16. Web cache poisoning (13 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Practitioner | Web cache poisoning with an unkeyed header | ⬜ Not Pwned | [📝](#) |
| Practitioner | Web cache poisoning with an unkeyed cookie | ⬜ Not Pwned | [📝](#) |
| Practitioner | Web cache poisoning with multiple headers | ⬜ Not Pwned | [📝](#) |
| Practitioner | Targeted web cache poisoning using an unknown header | ⬜ Not Pwned | [📝](#) |
| Practitioner | Web cache poisoning via an unkeyed query string | ⬜ Not Pwned | [📝](#) |
| Practitioner | Web cache poisoning via an unkeyed query parameter | ⬜ Not Pwned | [📝](#) |
| Practitioner | Parameter cloaking | ⬜ Not Pwned | [📝](#) |
| Practitioner | Web cache poisoning via a fat GET request | ⬜ Not Pwned | [📝](#) |
| Practitioner | URL normalization | ⬜ Not Pwned | [📝](#) |
| Expert | Web cache poisoning to exploit a DOM vulnerability via a cache with strict cacheability criteria | ⬜ Not Pwned | [📝](#) |
| Expert | Combining web cache poisoning vulnerabilities | ⬜ Not Pwned | [📝](#) |
| Expert | Cache key injection | ⬜ Not Pwned | [📝](#) |
| Expert | Internal cache poisoning | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>17. Insecure deserialization (10 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Modifying serialized objects | ⬜ Not Pwned | [📝](#) |
| Practitioner | Modifying serialized data types | ⬜ Not Pwned | [📝](#) |
| Practitioner | Using application functionality to exploit insecure deserialization | ⬜ Not Pwned | [📝](#) |
| Practitioner | Arbitrary object injection in PHP | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting Java deserialization with Apache Commons | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting PHP deserialization with a pre-built gadget chain | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting Ruby deserialization using a documented gadget chain | ⬜ Not Pwned | [📝](#) |
| Expert | Developing a custom gadget chain for Java deserialization | ⬜ Not Pwned | [📝](#) |
| Expert | Developing a custom gadget chain for PHP deserialization | ⬜ Not Pwned | [📝](#) |
| Expert | Using PHAR deserialization to deploy a custom gadget chain | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>18. Information disclosure (5 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Information disclosure in error messages | ⬜ Not Pwned | [📝](#) |
| Apprentice | Information disclosure on debug page | ⬜ Not Pwned | [📝](#) |
| Apprentice | Source code disclosure via backup files | ⬜ Not Pwned | [📝](#) |
| Apprentice | Authentication bypass via information disclosure | ⬜ Not Pwned | [📝](#) |
| Practitioner | Information disclosure in version control history | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>19. Business logic vulnerabilities (11 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Excessive trust in client-side controls | ⬜ Not Pwned | [📝](#) |
| Apprentice | High-level logic vulnerability | ⬜ Not Pwned | [📝](#) |
| Apprentice | Inconsistent security controls | ⬜ Not Pwned | [📝](#) |
| Apprentice | Flawed enforcement of business rules | ⬜ Not Pwned | [📝](#) |
| Practitioner | Low-level logic flaw | ⬜ Not Pwned | [📝](#) |
| Practitioner | Inconsistent handling of exceptional input | ⬜ Not Pwned | [📝](#) |
| Practitioner | Weak isolation on dual-use endpoint | ⬜ Not Pwned | [📝](#) |
| Practitioner | Insufficient workflow validation | ⬜ Not Pwned | [📝](#) |
| Practitioner | Authentication bypass via flawed state machine | ⬜ Not Pwned | [📝](#) |
| Practitioner | Infinite money logic flaw | ⬜ Not Pwned | [📝](#) |
| Practitioner | Authentication bypass via encryption oracle | ⬜ Not Pwned | [📝](#) |
| Expert | Bypassing access controls using email address parsing discrepancies | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>20. HTTP Host header attacks (7 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Basic password reset poisoning | ⬜ Not Pwned | [📝](#) |
| Apprentice | Host header authentication bypass | ⬜ Not Pwned | [📝](#) |
| Practitioner | Web cache poisoning via ambiguous requests | ⬜ Not Pwned | [📝](#) |
| Practitioner | Routing-based SSRF | ⬜ Not Pwned | [📝](#) |
| Practitioner | SSRF via flawed request parsing | ⬜ Not Pwned | [📝](#) |
| Practitioner | Host validation bypass via connection state attack | ⬜ Not Pwned | [📝](#) |
| Expert | Password reset poisoning via dangling markup | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>21. OAuth authentication (6 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Authentication bypass via OAuth implicit flow | ⬜ Not Pwned | [📝](#) |
| Practitioner | SSRF via OpenID dynamic client registration | ⬜ Not Pwned | [📝](#) |
| Practitioner | Forced OAuth profile linking | ⬜ Not Pwned | [📝](#) |
| Practitioner | OAuth account hijacking via redirect_uri | ⬜ Not Pwned | [📝](#) |
| Practitioner | Stealing OAuth access tokens via an open redirect | ⬜ Not Pwned | [📝](#) |
| Expert | Stealing OAuth access tokens via a proxy page | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>22. File upload vulnerabilities (7 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Remote code execution via web shell upload | ⬜ Not Pwned | [📝](#) |
| Apprentice | Web shell upload via Content-Type restriction bypass | ⬜ Not Pwned | [📝](#) |
| Practitioner | Web shell upload via path traversal | ⬜ Not Pwned | [📝](#) |
| Practitioner | Web shell upload via extension blacklist bypass | ⬜ Not Pwned | [📝](#) |
| Practitioner | Web shell upload via obfuscated file extension | ⬜ Not Pwned | [📝](#) |
| Practitioner | Remote code execution via polyglot web shell upload | ⬜ Not Pwned | [📝](#) |
| Expert | Web shell upload via race condition | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>23. JWT (8 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | JWT authentication bypass via unverified signature | ⬜ Not Pwned | [📝](#) |
| Apprentice | JWT authentication bypass via flawed signature verification | ⬜ Not Pwned | [📝](#) |
| Practitioner | JWT authentication bypass via weak signing key | ⬜ Not Pwned | [📝](#) |
| Practitioner | JWT authentication bypass via jwk header injection | ⬜ Not Pwned | [📝](#) |
| Practitioner | JWT authentication bypass via jku header injection | ⬜ Not Pwned | [📝](#) |
| Practitioner | JWT authentication bypass via kid header path traversal | ⬜ Not Pwned | [📝](#) |
| Expert | JWT authentication bypass via algorithm confusion | ⬜ Not Pwned | [📝](#) |
| Expert | JWT authentication bypass via algorithm confusion with no exposed key | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>24. Essential skills (2 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Practitioner | Discovering vulnerabilities quickly with targeted scanning | ⬜ Not Pwned | [📝](#) |
| Practitioner | Scanning non-standard data structures | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>25. Prototype pollution (10 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Practitioner | Client-side prototype pollution via browser APIs | ⬜ Not Pwned | [📝](#) |
| Practitioner | DOM XSS via client-side prototype pollution | ⬜ Not Pwned | [📝](#) |
| Practitioner | DOM XSS via an alternative prototype pollution vector | ⬜ Not Pwned | [📝](#) |
| Practitioner | Client-side prototype pollution via flawed sanitization | ⬜ Not Pwned | [📝](#) |
| Practitioner | Client-side prototype pollution in third-party libraries | ⬜ Not Pwned | [📝](#) |
| Practitioner | Privilege escalation via server-side prototype pollution | ⬜ Not Pwned | [📝](#) |
| Practitioner | Detecting server-side prototype pollution without polluted property reflection | ⬜ Not Pwned | [📝](#) |
| Practitioner | Bypassing flawed input filters for server-side prototype pollution | ⬜ Not Pwned | [📝](#) |
| Practitioner | Remote code execution via server-side prototype pollution | ⬜ Not Pwned | [📝](#) |
| Expert | Exfiltrating sensitive data via server-side prototype pollution | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>26. GraphQL API vulnerabilities (5 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Accessing private GraphQL posts | ⬜ Not Pwned | [📝](#) |
| Practitioner | Accidental exposure of private GraphQL fields | ⬜ Not Pwned | [📝](#) |
| Practitioner | Finding a hidden GraphQL endpoint | ⬜ Not Pwned | [📝](#) |
| Practitioner | Bypassing GraphQL brute force protections | ⬜ Not Pwned | [📝](#) |
| Practitioner | Performing CSRF exploits over GraphQL | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>27. Race conditions (6 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Limit overrun race conditions | ⬜ Not Pwned | [📝](#) |
| Practitioner | Bypassing rate limits via race conditions | ⬜ Not Pwned | [📝](#) |
| Practitioner | Multi-endpoint race conditions | ⬜ Not Pwned | [📝](#) |
| Practitioner | Single-endpoint race conditions | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting time-sensitive vulnerabilities | ⬜ Not Pwned | [📝](#) |
| Expert | Partial construction race conditions | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>28. NoSQL injection (4 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Detecting NoSQL injection | ⬜ Not Pwned | [📝](#) |
| Apprentice | Exploiting NoSQL operator injection to bypass authentication | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting NoSQL injection to extract data | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting NoSQL operator injection to extract unknown fields | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>29. API testing (5 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Exploiting an API endpoint using documentation | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting server-side parameter pollution in a query string | ⬜ Not Pwned | [📝](#) |
| Practitioner | Finding and exploiting an unused API endpoint | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting a mass assignment vulnerability | ⬜ Not Pwned | [📝](#) |
| Expert | Exploiting server-side parameter pollution in a REST URL | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>30. Web LLM attacks (4 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Exploiting LLM APIs with excessive agency | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting vulnerabilities in LLM APIs | ⬜ Not Pwned | [📝](#) |
| Practitioner | Indirect prompt injection | ⬜ Not Pwned | [📝](#) |
| Expert | Exploiting insecure output handling in LLMs | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>31. Web cache deception (5 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | Exploiting path mapping for web cache deception | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting path delimiters for web cache deception | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting origin server normalization for web cache deception | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting cache server normalization for web cache deception | ⬜ Not Pwned | [📝](#) |
| Expert | Exploiting exact-match cache rules for web cache deception | ⬜ Not Pwned | [📝](#) |
</details>

---
