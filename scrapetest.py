
import re, urllib
import requests
from BeautifulSoup import BeautifulSoup


urlobject = requests.get('http://www.digitalscholar.net')
#print(urlobject)

urltext = urlobject.text
#print(urltext)

soup = BeautifulSoup(urltext)
#print(soup)

urls1 = soup.findAll('a',href=True)
# print(urls1[0])
# Try other tags!

#for tag in urls1:
#    print(tag['href'])

urlslist = []
for tag in urls1:
    urlslist.append(tag['href'])

#for item in urlslist:
#    print(item)

# Remove duplicates

urlslist = set(urlslist)

def compile_site_urls(list):
    output = []
    domain = "www.digitalscholar.net"
    for url in list:
        if domain in url:
            url = requests.get(url)
            url = url.text
            try:
                soup = BeautifulSoup(url)
            except(UnicodeEncodeError):
                pass
            urlslist = soup.findAll('a',href=True)
            for urlitem in urlslist:
                output.append(urlitem['href'])
    return output

#sitescrape = compile_site_urls(urlslist)

    


