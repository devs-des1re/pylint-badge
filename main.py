import os, subprocess, re

path = os.sys.argv[1] if len(os.sys.argv) > 1 else "."

# Run pylint
result = subprocess.run(["pylint", path], capture_output=True, text=True)
match = re.search(r"rated at ([\d\.]+)/10", result.stdout)
score = float(match.group(1)) if match else 0.0

# Generate badge SVG
if score < 4: color = "red"
elif score < 7: color = "orange"
elif score < 9: color = "yellowgreen"
else: color = "green"

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="150" height="20">
<rect width="70" height="20" fill="#555"/>
<rect x="70" width="80" height="20" fill="{color}"/>
<text x="35" y="14" fill="#fff" font-family="Verdana" font-size="11" text-anchor="middle">pylint</text>
<text x="110" y="14" fill="#fff" font-family="Verdana" font-size="11" text-anchor="middle">{score:.2f}/10</text>
</svg>"""

os.makedirs("badges", exist_ok=True)
with open("badges/pylint.svg", "w") as f:
    f.write(svg)

# Push to gh-pages using GITHUB_TOKEN
token = os.environ.get("GITHUB_TOKEN")
subprocess.run(["git", "config", "--global", "user.name", "github-actions"])
subprocess.run(["git", "config", "--global", "user.email", "github-actions@github.com"])
subprocess.run(["git", "checkout", "-B", "gh-pages"])
subprocess.run(["cp", "-r", "badges/*", "."])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Update pylint badge"], check=False)
subprocess.run(["git", "push", f"https://x-access-token:{token}@github.com/{os.environ['GITHUB_REPOSITORY']}.git", "gh-pages", "--force"])
