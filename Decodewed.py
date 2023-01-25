import requests
from bs4 import BeautifulSoup

#print out a list of all the article titles on NewYork times homepage
#get Newyork Times
r = requests.get("https://www.nytimes.com/")
#print out list of articles titles
soup = BeautifulSoup(r.text)

for headline in soup.find_all(class__="headline"):
    if headline.a:
        print(headline.a.text.replace("/n"," ").strip())
    else:
        print(headline.contents[0].strip())
