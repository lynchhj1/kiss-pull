#Import the packages
import os
import shutil, requests, sys, re, glob, zipfile
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

#Assign the URL to a variable
try:
    url = sys.argv[1]
except:
    print('Add url after script name')
    print('Usage: python3',sys.argv[0],'https://kissmanga.org/manga/manga-pb992910')
    sys.exit(1)  # abort

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#First open, then read the the HTML
html_doc = urlopen(req).read()
soup = BeautifulSoup(html_doc, 'html.parser')

link_list = []
chapter_found = False
base_url='https://kissmanga.org'
links = soup.find_all("a", attrs={'href': re.compile("^/chapter")})
for link in links:
  full_url=base_url+link.get("href")
  link_list.append(full_url)
link_list.reverse()

##print(link_list)

for x in link_list:
   print(x)

