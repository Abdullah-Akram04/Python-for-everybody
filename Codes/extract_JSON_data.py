import urllib.request
import json

# Get URL from user
url = input("Enter location: ")

# Read data from URL
print("Retrieving", url)
data = urllib.request.urlopen(url).read().decode()

print("Retrieved", len(data), "characters")

# Parse JSON
info = json.loads(data)

# Initialize sum
total = 0

# Extract comment counts
for item in info["comments"]:
    total += item["count"]

# Print result
print("Count:", len(info["comments"]))
print("Sum:", total)