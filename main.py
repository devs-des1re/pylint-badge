import subprocess, re, os

# Run pylint
result = subprocess.run(["pylint", "."], capture_output=True, text=True)
match = re.search(r"rated at ([\d\.]+)/10", result.stdout)
score = float(match.group(1)) if match else 0.0

# Choose badge color
if score < 4: color = "red"
elif score < 7: color = "orange"
elif score < 9: color = "yellowgreen"
else: color = "green"

# Make SVG
svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="150" height="20">
  <rect width="70" height="20" fill="#555"/>
  <rect x="70" width="80" height="20" fill="{color}"/>
  <text x="35" y="14" fill="#fff" font-family="Verdana" font-size="11" text-anchor="middle">pylint</text>
  <text x="110" y="14" fill="#fff" font-family="Verdana" font-size="11" text-anchor="middle">{score:.2f}/10</text>
</svg>
"""

# Save badge
os.makedirs("badges", exist_ok=True)
with open("badges/pylint.svg", "w") as f:
    f.write(svg)
