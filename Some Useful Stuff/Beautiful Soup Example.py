import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://github.com/').read()

soup = bs.BeautifulSoup(source,'lxml')

#print(soup)

# title of the page
print(soup.title)
# get attributes:
print(soup.title.name)
# get values:
print(soup.title.string)
#beginning navigation:
print(soup.title.parent.name)
# getting specific values:
#print(soup.p)

print(soup.find_all('p')) #finds all paragraph tags
for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))
    
for url in soup.find_all('a'):
    print(url.get('href'))

print(soup.get_text())

# Nav bar
nav = soup.nav
for url in nav.find_all('a'):
    print(url.get('href'))
    
# Body
body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)
    
# Divs
for div in soup.find_all('div', class_='body'):
    print(div.text)