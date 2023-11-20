#Import the packages
import os
import shutil, requests, sys, re, glob, zipfile
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

#Assign the URL to variable and set agent to get around mod_security
# https://stackoverflow.com/questions/16627227/problem-http-error-403-in-python-3-web-scraping
try:
    url = sys.argv[1]
except:
    print('Add url after script name')
    print('Usage: python3',sys.argv[0],'https://kissmanga.org/chapter/manga-qj952992/chapter-1')
    sys.exit(1)  # abort

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

if not os.path.exists('download'):
   os.makedirs('download')

#First open, then read the the HTML
html_doc = urlopen(req).read()
soup = BeautifulSoup(html_doc, 'html.parser')
 
#Pull title and convert to string so re can be used on it to get manga name
#print(soup.prettify())
replacements = [
    (r'<Title>Read ', ''),
    (r' Online Free | Kissmanga</Title>', ''),
    (r'\|',''),
    (r' ','.')
]

ugly_title = str(soup.title)
ugly_title = ugly_title.title()

for old, new in replacements:
    ugly_title = re.sub(old, new, ugly_title)

#Figure out how many 0s to fill in issue # with
chapter=url.rsplit('/', 1)[-1]
chapter_clean = chapter.rsplit('-', 1)[-1]
try:
    whole_chapter_num = len(chapter_clean.rsplit('.', 1)[1])
except:
    whole_chapter_num = len(chapter_clean)

zero_fill_amt = (4-whole_chapter_num)*"0"
issue_name='../'+ugly_title+'.'+zero_fill_amt+chapter_clean+'.cbz'

#Get all the img src http links
image_data = []

for link in soup.findAll('img'):
    if "https" in link.get('src'):
        lnk = link.get('src')
        image_data.append((lnk))


#Download all image files with properly numbered names
for i in range(len(image_data)):
    response = requests.get(image_data[i], stream=True)
    real_name=('download/'+str(i).zfill(3))+".jpg"
    file = open(real_name, 'wb')
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)

#Zip files into cbz and delete download folder
os.chdir("download/")
with zipfile.ZipFile(issue_name, 'w') as f:
    for file in glob.glob('*.jpg'):
        f.write(file)
os.chdir("..")
shutil.rmtree('download')

