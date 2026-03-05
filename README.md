# PortSwigger Web Security Academy - Lab Tracker

[![Overall Progress](https://img.shields.io/badge/Progress-0%2F245%20Labs-red?style=for-the-badge&logo=target)](https://portswigger.net/web-security)
[![Burp Suite](https://img.shields.io/badge/Tools-BurpSuite%20%7C%20OWASP-orange?style=for-the-badge)](https://portswigger.net/burp)
[![Status](https://img.shields.io/badge/Status-Initializing...-lightgrey?style=for-the-badge)]()

A systematic roadmap to mastering web application security. This repository tracks my hands-on journey through the PortSwigger Academy, documenting every vulnerability pwned and every technique learned.

---

## Progress Dashboard

| Vulnerability Category | Completed | Status |
| :--- | :---: | :--- |
| [SQL Injection](#1-sql-injection) | 0 / 18 | 🌑 Not Started |
| [Cross-Site Scripting (XSS)](#2-cross-site-scripting) | 0 / 30 | 🌑 Not Started |
| [CSRF](#3-cross-site-request-forgery) | 0 / 12 | 🌑 Not Started |
| [OS Command Injection](#4-os-command-injection) | 0 / 5 | 🌑 Not Started |
| **Total Academy Progress** | **0 / 245** | **0%** |

---

## Vulnerability List & Lab Tracker

<details>
<summary><b>1. SQL Injection (18 Labs) </b></summary>

> **Description:** Manipulating backend SQL queries.
> **Impact:** Data exfiltration, Authentication bypass.

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | SQLi in WHERE clause (Hidden data) | ⬜ Not Pwned | [📝](#) |
| Apprentice | SQLi allowing login bypass | ⬜ Not Pwned | [📝](#) |
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
| Apprentice | Reflected XSS into HTML (No encoding) | ⬜ Not Pwned | [📝](#) |
| Apprentice | Stored XSS into HTML (No encoding) | ⬜ Not Pwned | [📝](#) |
| Apprentice | DOM XSS in `document.write` sink | ⬜ Not Pwned | [📝](#) |
| Practitioner | Exploiting XSS to steal cookies | ⬜ Not Pwned | [📝](#) |
| Expert | Reflected XSS with sandbox escape | ⬜ Not Pwned | [📝](#) |
</details>

<details>
<summary><b>3. Cross-Site Request Forgery (CSRF) (12 Labs) </b></summary>

| Level | Lab Title | Status | Writeup |
| :--- | :--- | :---: | :---: |
| Apprentice | CSRF with no defenses | ⬜ Not Pwned | [📝](#) |
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

## The Pentester's Kit
* **Proxy:** Burp Suite Professional / Community
* **Browser:** Firefox (with FoxyProxy)
* **Extensions:** Turbo Intruder, Hackvertor, Param Miner

---
