import os
import requests

# Check if README.md exists, if not create it
if not os.path.exists("README.md"):
    # Create an empty README.md file
    with open("README.md", "w") as file:
        file.write("")
    print("README.md has been created.")

# Download README.md from the specified URL
url = 'https://raw.githubusercontent.com/acymz/AutoData/main/README.md'
response = requests.get(url)
response.raise_for_status()

# Save README.md to the current directory
with open('README.md', 'wb') as file:
    file.write(response.content)

print('README.md has been downloaded.')
