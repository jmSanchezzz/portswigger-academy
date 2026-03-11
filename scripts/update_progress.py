import os
import re

README = "README.md"
WRITEUPS = "writeups"

TOTAL_LABS = 251

CATEGORY_MAP = {
    "sql-injection": "1. SQL Injection",
    "xss": "2. Cross-Site Scripting (XSS)",
    "csrf": "3. CSRF",
    "clickjacking": "4. Clickjacking",
    "dom-vulnerabilities": "5. DOM-based vulnerabilities",
    "cors": "6. CORS",
    "xxe": "7. XXE Injection",
    "ssrf": "8. SSRF",
    "os-command-injection": "10. OS command injection",
    "path-traversal": "12. Path traversal", 
    "access-control": "13. Access control vulnerabilities",
    "websockets": "15. WebSockets"
    "authentication": "14. Authentication"
}

def get_writeups():
    solved = {}
    if not os.path.exists(WRITEUPS):
        return solved

    for category in os.listdir(WRITEUPS):
        path = os.path.join(WRITEUPS, category)
        if not os.path.isdir(path):
            continue

        labs = []
        for folder in os.listdir(path):
            lab_path = os.path.join(path, folder)
            
            if folder.startswith(".") or not os.path.isdir(lab_path):
                continue
            
            labs.append(folder)
            
        solved[category] = labs
    return solved

def update_lab_table(content, solved):
    for category, labs in solved.items():
        for lab in labs:
            try:
                raw_title_part = lab.split("_", 1)[1]
                
                words = [word for word in raw_title_part.split("_") if word]
            except IndexError:
                continue 
            
            fuzzy_title = r"[\s,\.\-:]+".join(re.escape(word) for word in words)
            
            pattern = re.compile(rf"^\|\s*(.*?)\s*\|\s*({fuzzy_title})\s*\|.*?\|.*?\|.*$", re.MULTILINE | re.IGNORECASE)
            
            replacement = f"| \\1 | \\2 | ✅ Pwned | [📝](./writeups/{category}/{lab}/README.md) |"
            
            content = pattern.sub(replacement, content)
            
    return content

def update_dashboard(content, solved):
    total_solved = sum(len(labs) for labs in solved.values())
    percentage = int((total_solved / TOTAL_LABS) * 100)

    content = re.sub(
        r"\*\*Total Academy Progress\*\* \| \*\*\d+ / 251\*\* \| \*\*\d+%\*\*",
        f"**Total Academy Progress** | **{total_solved} / 251** | **{percentage}%**",
        content
    )

    content = re.sub(
        r"badge/Progress-\d+%2F251",
        f"badge/Progress-{total_solved}%2F251",
        content
    )
    return content

def update_category_counts(content, solved):
    for category in solved:
        count = len(solved[category])
        
        pattern = rf"\|\s*\[(\d+\.\s*.*?)\]\(#.*?\)\s*\|\s*\d+\s*/\s*(\d+)\s*\|\s*(.*?)\|"

        def repl(match):
            title = match.group(1)
            total = match.group(2)

            mapped_name = CATEGORY_MAP.get(category)

            if mapped_name and mapped_name in title:
                status = "Mastered" if count == int(total) else "In Progress" if count > 0 else "Not Started"
                
                clean_anchor = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
                
                return f"| [{title}](#{clean_anchor}-{total}-labs) | {count} / {total} | {status} |"
            
            return match.group(0)

        content = re.sub(pattern, repl, content)
        
    return content

def main():
    with open(README, "r", encoding="utf-8") as f:
        content = f.read()

    solved = get_writeups()

    content = update_lab_table(content, solved)
    content = update_category_counts(content, solved)
    content = update_dashboard(content, solved)

    with open(README, "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ README progress updated successfully!")

if __name__ == "__main__":
    main()

