#! Python27
## ToDo: Add depth parameter

import re, urllib
import requests
from BeautifulSoup import BeautifulSoup


## Enter start point and domain delimiter

##starturl = "http://www.digitalscholar.net"
domain = 'interviews' ## URLs must contain this string to be recognized
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

## Output file
textfile = open('FILENAME','w')


## Define functions

## Finds all URLs on a page and returns them in a list
def pull_urls(starturl,domain):
## Originally used regular expressions, which looked like this:
##    x = re.findall(r'''href=["'](.[^"']+)["']''', urllib.urlopen(starturl).read(), re.I)
    list1 = []
    list2 = []
    x = requests.get(starturl)
    x = x.text
    soup = BeautifulSoup(x)
    for tag in soup.findAll('a', href=True):
        list1.append(tag['href'])
    for item in list1:
        if domain in item:
            list2.append(item)
    return list2

## Takes a list of URLs, follows them, and compiles a list of URLs on those pages
def follow_down(urls,domain):
    biglist = []
    for url in urls:
        level2 = pull_urls(url,domain)
        for url2 in level2:
            biglist.append(url2)
    return biglist

## Writes to .txt file
def writetofile(item,textfile):
    for x in item:
        textfile.write(x+'\n')


###############


## Call the follow_down function, passin gin our list of URLs and domain limiter
endlist = follow_down(start_urls,domain)

## Clean up our master list of URLs by removing undesired items
baditems = ['/interviews/name/#list','/interviews/#list','/interviews/#list','/interviews']
for baditem in baditems:
    while baditem in endlist:
        endlist.remove(baditem)

## Use set function to delete redundant items in our list
endlist = set(endlist)

## Turn set item back into usable text
endlist = list(endlist)

## Pull the HTML from each of our links and put in text files
for pagelink in endlist:
    g = requests.get(r'http://www.theparisreview.org'+pagelink) ## The r makes it a "raw string." Simplifies the / and // syntax a bit.
    g = g.text ## Make the "requests" object into a string
    g = g.encode("utf8","ignore") ## Tells what kind of format the string will be in. If you leave it out the code will kind of work, but will throw bizarre errors every few documents. Text encoding extremely finicky area

## Uncomment to see the HTML of the first item for testing purposes
##    print(g)
##    break

## Write HTMLto file (note this is still in the for loop above)

## Use string functions to get the title
    titlestart = g.find('<title>') + 7
    titleend = g.find('</title>')
    itemtitle = g[titlestart:titleend]

## Create the file with the title as the name and write the HTML to it
    textfile1 = open(itemtitle+'.txt','w')
    textfile1.write(g)

## Close the file, for loop goes to next URL in the list
    textfile1.close()


