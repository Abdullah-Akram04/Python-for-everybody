import urllib.request
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/comments_2434384.html"

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# find all span tags (this is where numbers are stored)
tags = soup.find_all("span")

total = 0

for tag in tags:
    total += int(tag.text)

print("Sum:", total)
