import urllib.request, urllib.parse, urllib.error   

url = input('Enter URL: ')
fhand = urllib.request.urlopen("https://books.toscrape.com/?utm_source=chatgpt.com")
for line in fhand:
    print(line.decode().strip())