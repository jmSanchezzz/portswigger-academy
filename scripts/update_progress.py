import re

readme_path = 'README.md'

# 1. Read the current README
with open(readme_path, 'r', encoding='utf-8') as file:
    content = file.read()

# 2. Define your categories (Dashboard Name, Section Title, Total Labs)
categories = [
    ("1. SQL Injection", "1. SQL Injection", 18),
    ("2. Cross-Site Scripting (XSS)", "2. Cross-Site Scripting (XSS)", 30),
    ("3. CSRF", "3. Cross-Site Request Forgery (CSRF)", 12),
    ("4. Clickjacking", "4. Clickjacking", 5),
    ("5. DOM-based vulnerabilities", "5. DOM-based vulnerabilities", 7),
    ("6. CORS", "6. Cross-origin resource sharing (CORS)", 3),
    ("7. XXE Injection", "7. XML external entity (XXE) injection", 9),
    ("8. SSRF", "8. Server-side request forgery (SSRF)", 7),
    ("9. HTTP request smuggling", "9. HTTP request smuggling", 21),
    ("10. OS command injection", "10. OS command injection", 5),
    ("11. Server-side template injection", "11. Server-side template injection", 7),
    ("12. Path traversal", "12. Path traversal", 6),
    ("13. Access control vulnerabilities", "13. Access control vulnerabilities", 13),
    ("14. Authentication", "14. Authentication", 14),
    ("15. WebSockets", "15. WebSockets", 3),
    ("16. Web cache poisoning", "16. Web cache poisoning", 13),
    ("17. Insecure deserialization", "17. Insecure deserialization", 10),
    ("18. Information disclosure", "18. Information disclosure", 5),
    ("19. Business logic vulnerabilities", "19. Business logic vulnerabilities", 11),
    ("20. HTTP Host header attacks", "20. HTTP Host header attacks", 7),
    ("21. OAuth authentication", "21. OAuth authentication", 6),
    ("22. File upload vulnerabilities", "22. File upload vulnerabilities", 7),
    ("23. JWT", "23. JWT", 8),
    ("24. Essential skills", "24. Essential skills", 2),
    ("25. Prototype pollution", "25. Prototype pollution", 10),
    ("26. GraphQL API vulnerabilities", "26. GraphQL API vulnerabilities", 5),
    ("27. Race conditions", "27. Race conditions", 6),
    ("28. NoSQL injection", "28. NoSQL injection", 4),
    ("29. API testing", "29. API testing", 5),
    ("30. Web LLM attacks", "30. Web LLM attacks", 4),
    ("31. Web cache deception", "31. Web cache deception", 5)
]

total_pwned = 0
total_all_labs = 251

# 3. Process each category individually
for dash_name, section_title, total_labs in categories:
    # Use Regex to isolate the block between the <summary> and </details> for this category
    section_pattern = rf'<summary><b>{re.escape(section_title)}.*?</details>'
    section_match = re.search(section_pattern, content, re.DOTALL)

    if section_match:
        section_text = section_match.group(0)
        
        # Count the Pwned tags only inside this specific section
        pwned_count = section_text.count('✅ Pwned')
        total_pwned += pwned_count

        # Auto-determine the status (Emojis removed)
        if pwned_count == total_labs:
            status = "Mastered"
        elif pwned_count > 0:
            status = "In Progress"
        else:
            status = "Not Started"

        # Update the specific row in the Dashboard table (preserves your anchor links)
        row_pattern = rf'(\|\s*\[{re.escape(dash_name)}\]\([^)]+\)\s*\|\s*)\d+(\s*/\s*{total_labs}\s*\|\s*)[^|]+(\s*\|)'
        replacement = rf'\g<1>{pwned_count}\g<2>{status}\g<3>'
        content = re.sub(row_pattern, replacement, content)

# 4. Calculate overall percentage
percentage = int((total_pwned / total_all_labs) * 100)

# 5. Update the Grand Total Row
total_pattern = r'(\|\s*\*\*Total Academy Progress\*\*\s*\|\s*\*\*)\d+(\s*/\s*251\*\*\s*\|\s*\*\*)\d+(%\*\*\s*\|)'
content = re.sub(total_pattern, rf'\g<1>{total_pwned}\g<2>{percentage}\g<3>', content)

# 6. Update the Top Badge
badge_pattern = r'badge/Progress-\d+%2F251'
new_badge = f'badge/Progress-{total_pwned}%2F251'
content = re.sub(badge_pattern, new_badge, content)

# 7. Write all changes back to the README
with open(readme_path, 'w', encoding='utf-8') as file:
    file.write(content)

print(f"✅ Auto-update complete: {total_pwned}/251 ({percentage}%) overall.")
