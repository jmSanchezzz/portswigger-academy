import re

readme_path = 'README.md'

# 1. Read the current README
with open(readme_path, 'r', encoding='utf-8') as file:
    content = file.read()

# 2. Define your categories (Dashboard Name, Section Title, Total Labs)
categories = [
    ("SQL Injection", "1. SQL Injection", 18),
    ("Cross-Site Scripting (XSS)", "2. Cross-Site Scripting (XSS)", 30),
    ("CSRF", "3. Cross-Site Request Forgery (CSRF)", 12),
    ("OS Command Injection", "4. OS Command Injection", 5)
]

total_pwned = 0
total_all_labs = 245

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

        # Auto-determine the status emoji
        if pwned_count == total_labs:
            status = "🏆 Mastered"
        elif pwned_count > 0:
            status = "🚧 In Progress"
        else:
            status = "🌑 Not Started"

        # Update the specific row in the Dashboard table (preserves your anchor links)
        row_pattern = rf'(\|\s*\[{re.escape(dash_name)}\]\([^)]+\)\s*\|\s*)\d+(\s*/\s*{total_labs}\s*\|\s*)[^|]+(\s*\|)'
        replacement = rf'\g<1>{pwned_count}\g<2>{status}\g<3>'
        content = re.sub(row_pattern, replacement, content)

# 4. Calculate overall percentage
percentage = int((total_pwned / total_all_labs) * 100)

# 5. Update the Grand Total Row
total_pattern = r'(\|\s*\*\*Total Academy Progress\*\*\s*\|\s*\*\*)\d+(\s*/\s*245\*\*\s*\|\s*\*\*)\d+(%\*\*\s*\|)'
content = re.sub(total_pattern, rf'\g<1>{total_pwned}\g<2>{percentage}\g<3>', content)

# 6. Update the Top Badge
badge_pattern = r'badge/Progress-\d+%2F245'
new_badge = f'badge/Progress-{total_pwned}%2F245'
content = re.sub(badge_pattern, new_badge, content)

# 7. Write all changes back to the README
with open(readme_path, 'w', encoding='utf-8') as file:
    file.write(content)

print(f"✅ Auto-update complete: {total_pwned}/245 ({percentage}%) overall.")
