import json

# Load user data
with open('data/user.json', 'r', encoding='utf-8') as file:
    user = json.load(file)

# Load template
with open('templates/simple.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Format lists
skills_html = ''.join(f"<li>{skill}</li>" for skill in user["skills"])
projects_html = ''.join(
    f'<li><a href="{proj["link"]}">{proj["title"]}</a>: {proj["description"]}</li>'
    for proj in user["projects"]
)

# Replace placeholders
output = (
    template
    .replace("{{ name }}", user["name"])
    .replace("{{ bio }}", user["bio"])
    .replace("{{ skills }}", skills_html)
    .replace("{{ projects }}", projects_html)
    .replace("{{ email }}", user["contact"]["email"])
    .replace("{{ github }}", user["contact"]["github"])
)

# Write to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(output)

print("✅ Portfolio generated! Open 'index.html' to view it.")
