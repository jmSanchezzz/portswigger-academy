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
    "os-command-injection": "10. OS command injection", # BUG FIX 1: Matches your folder name perfectly
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
                # Splits "1_OS_command_injection_simple_case" into words: ['OS', 'command', 'injection', 'simple', 'case']
                words = lab.split("_", 1)[1].split("_")
            except IndexError:
                continue 
            
            # BUG FIX 2: Fuzzy matching! 
            # This allows commas, hyphens, colons, or multiple spaces between words.
            fuzzy_title = r"[\s,\.\-:]+".join(re.escape(word) for word in words)
            
            # The regex now uses the fuzzy title to hunt down the row
            pattern = re.compile(rf"^\|\s*(.*?)\s*\|\s*({fuzzy_title})\s*\|.*?\|.*?\|.*$", re.MULTILINE | re.IGNORECASE)
            
            # \2 preserves the original exact title from the table (including its comma)
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
