import subprocess, re, json, os

# Run pylint
result = subprocess.run(["pylint", "."], capture_output=True, text=True)
match = re.search(r"rated at ([\d\.]+)/10", result.stdout)
score = float(match.group(1)) if match else 0.0

# Determine color
if score < 4: color = "red"
elif score < 7: color = "orange"
elif score < 9: color = "yellowgreen"
else: color = "green"

# Create JSON for Shields.io
badge = {
    "schemaVersion": 1,
    "label": "pylint",
    "message": f"{score:.2f}/10",
    "color": color
}

os.makedirs("badges", exist_ok=True)
with open("badges/pylint.json", "w") as f:
    json.dump(badge, f)
