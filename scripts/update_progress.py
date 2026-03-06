import os
import re

README = "README.md"
WRITEUPS = "writeups"

TOTAL_LABS = 251

CATEGORY_MAP = {
    "sql-injection": "SQL Injection",
    "xss": "Cross-Site Scripting",
    "csrf": "CSRF",
    "clickjacking": "Clickjacking",
    "dom-vulnerabilities": "DOM-based vulnerabilities",
    "cors": "CORS",
    "xxe": "XXE",
    "ssrf": "SSRF",
    "command-injection": "OS command injection"
}

def get_writeups():
    solved = {}

    for category in os.listdir(WRITEUPS):

        path = os.path.join(WRITEUPS, category)

        if not os.path.isdir(path):
            continue

        labs = []

        for folder in os.listdir(path):

            if folder.startswith("."):
                continue

            labs.append(folder)

        solved[category] = labs

    return solved


def update_lab_table(content, solved):

    for category, labs in solved.items():

        for lab in labs:

            lab_title = lab.split("_",1)[1].replace("_"," ")

            pattern = rf"\| (.*?) \| {re.escape(lab_title)} \| ⬜ Not Pwned \| \[📝\]\(#\) \|"

            replacement = f"| \\1 | {lab_title} | ✅ Pwned | [📝](./writeups/{category}/{lab}/README.md) |"

            content = re.sub(pattern, replacement, content)

    return content


def update_dashboard(content, solved):

    total_solved = 0

    for category in solved:

        total_solved += len(solved[category])

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

        pattern = rf"\|\s*\[(\d+\. .*?)\]\(#.*?\)\s*\|\s*\d+\s*/\s*(\d+)\s*\|\s*(.*?)\|"

        def repl(match):

            title = match.group(1)
            total = match.group(2)

            if CATEGORY_MAP.get(category) in title:

                status = "Mastered" if count == int(total) else "In Progress" if count > 0 else "Not Started"

                return f"| [{title}](#{title.lower().replace(' ','-')}-{total}-labs) | {count} / {total} | {status}|"

            return match.group(0)

        content = re.sub(pattern, repl, content)

    return content


def main():

    with open(README,"r",encoding="utf-8") as f:
        content = f.read()

    solved = get_writeups()

    content = update_lab_table(content, solved)
    content = update_category_counts(content, solved)
    content = update_dashboard(content, solved)

    with open(README,"w",encoding="utf-8") as f:
        f.write(content)

    print("README progress updated successfully")


if __name__ == "__main__":
    main()
