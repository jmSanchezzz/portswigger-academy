# PortSwigger Web Security Academy - Lab Tracker

[![Overall Progress](https://img.shields.io/badge/Progress-11%2F245%20Labs-red?style=for-the-badge&logo=target)](https://portswigger.net/web-security)
[![Burp Suite](https://img.shields.io/badge/Tools-BurpSuite%20%7C%20OWASP-orange?style=for-the-badge)](https://portswigger.net/burp)
[![Status](https://img.shields.io/badge/Status-Initializing...-lightgrey?style=for-the-badge)]()

A systematic roadmap to mastering web application security. This repository tracks my hands-on journey through the PortSwigger Academy, documenting every vulnerability pwned and every technique learned.

---

## Progress Dashboard

| Vulnerability Category | Completed | Status |
| :--- | :---: | :--- |
| [SQL Injection](#1-sql-injection-18-labs) | 2 / 18 | In Progress|
| [Cross-Site Scripting (XSS)](#2-cross-site-scripting-30-labs) | 9 / 30 | In Progress|
| [CSRF](#3-cross-site-request-forgery-12-labs) | 0 / 12 | Not Started|
| [OS Command Injection](#4-os-command-injection-5-labs) | 0 / 5 | Not Started|
| **Total Academy Progress** | **11 / 245** | **4%** |

---

## Vulnerability List & Lab Tracker

<details>
<summary><b>1. SQL Injection (18 Labs) </b></summary>

> **Description:** Manipulating backend SQL queries.
> **Impact:** Data exfiltration, Authentication bypass.

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

> **Description:** Injecting malicious scripts into trusted websites.
> **Impact:** Session hijacking, phishing, or unauthorized actions.

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
</details>

<details>
<summary><b>4. OS Command Injection (5 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | OS command injection, simple case | ⬜ Not Pwned | [📝](#) |
| Practitioner | Blind OS injection (Time delays) | ⬜ Not Pwned | [📝](#) |
| Practitioner | Blind OS injection (Output redirection) | ⬜ Not Pwned | [📝](#) |
</details>

---
