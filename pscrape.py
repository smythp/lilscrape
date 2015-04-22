#! Python27
## ToDo: Add depth parameter

import re, urllib
import requests
from BeautifulSoup import BeautifulSoup


## Enter start point and domain limiter
starturl = "http://www.digitalscholar.net"
domain = 'digitalscholar.net'



## Output file
textfile = open('paris1.txt','w')

def pull_urls(starturl,domain):
##    x = re.findall(r'''href=["'](.[^"']+)["']''', urllib.urlopen(starturl).read(), re.I)
    coollist = []
    finallist = []
    x = requests.get(starturl)
    x = x.text
    soup = BeautifulSoup(x)
    for tag in soup.findAll('a', href=True):
        coollist.append(tag['href'])
    for item in coollist:
        if domain in item:
            finallist.append(item)
    return finallist

def follow_down(urls1,domain):
    biglist = []
    for item in urls1:
        item_list = pull_urls(item,domain)
        for item2 in item_list:
            biglist.append(item2)
    return biglist
    
def writetofile(item,textfile):
    for x in item:
        textfile.write(x+'\n')

## Example
## Pull all links from a page
##xx = pull_urls(starturl,domain)
## Follow those links and pull links from THOSE pages
##yy = follow_down(xx,domain)



###############


start_urls = [
##    'http://www.digitalscholar.net'
        'http://www.theparisreview.org/interviews/name/#list',
        'http://www.theparisreview.org/interviews/name/D-F#list',
        'http://www.theparisreview.org/interviews/name/G-I#list',
        'http://www.theparisreview.org/interviews/name/J-L#list',
        'http://www.theparisreview.org/interviews/name/M-O#list',
        'http://www.theparisreview.org/interviews/name/P-R#list',
        'http://www.theparisreview.org/interviews/name/S-U#list',
        'http://www.theparisreview.org/interviews/name/V-Z#list',
        ]
endlist = []

for url_item in start_urls:
##    print('trying url: ',url_item)
    xx = pull_urls(url_item,domain)
##    print('On page:')
##    writetofile(xx,textfile)
    for line1 in xx:
        endlist.append(line1)


baditems = ['/interviews/name/#list','/interviews/#list','/interviews/#list','/interviews']
for baditem in baditems:
    while baditem in endlist:
        endlist.remove(baditem)

endlist = set(endlist)
endlist = list(endlist)

for pagelink in endlist:
    g = requests.get(r'http://www.theparisreview.org'+pagelink)
    g = g.text
    g = g.encode("utf8","ignore")
##    print(g)
##    break
    titlestart = g.find('<title>') + 7
    titleend = g.find('</title>')
    itemtitle = g[titlestart:titleend]
    textfile1 = open(itemtitle+'.txt','w')
    textfile1.write(g)
    textfile1.close()




##test
##for i in endlist:
##    print(i)

textfile.close()




## Uncomment to go one level deeper
##for url in urls1:
##    urls2 = pull_urls(url,domain)
##    textfile.write(urls2+'\n')





##
##for i in x):
##    for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
##        if "digitalscholar.net" in ee:
##            print(ee)
##            textfile.write(ee+'\n')
##    else:
##        continue

##
##for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(starturl).read(), re.I):
##    for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
##        if "digitalscholar.net" in ee:
##            print(ee)
##            textfile.write(ee+'\n')
##
