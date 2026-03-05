import re
import os

readme_path = 'README.md'

# 1. Read the current README
with open(readme_path, 'r', encoding='utf-8') as file:
    content = file.read()

# 2. Count total completed labs
pwned_count = content.count('✅ Pwned')
total_labs = 245
percentage = int((pwned_count / total_labs) * 100)

# 3. Update the Dashboard Total Row
row_pattern = r'\|\s*\*\*Total Academy Progress\*\*\s*\|\s*\*\*\d+\s*/\s*245\*\*\s*\|\s*\*\*\d+%\*\*\s*\|'
new_row = f'| **Total Academy Progress** | **{pwned_count} / {total_labs}** | **{percentage}%** |'
content = re.sub(row_pattern, new_row, content)

# 4. Update the Top Badge (Finds 'Progress-X%2F245')
badge_pattern = r'badge/Progress-\d+%2F245'
new_badge = f'badge/Progress-{pwned_count}%2F245'
content = re.sub(badge_pattern, new_badge, content)

# 5. Write changes back to the file
with open(readme_path, 'w', encoding='utf-8') as file:
    file.write(content)

print(f"✅ README updated: {pwned_count}/{total_labs} ({percentage}%) completed.")
