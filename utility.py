import bs4 as bs 
import subprocess
import urllib.parse
import sys
import os
import time

import random
import urllib.request


levelUrls = ["https://www.imabi.net/beginnersi.htm", "https://www.imabi.net/beginnersii.htm", 
"https://www.imabi.net/intermediatei.htm", "https://www.imabi.net/intermediateii.htm",
"https://www.imabi.net/advancedi.htm", "https://www.imabi.net/advancedii.htm",
"https://www.imabi.net/veterani.htm", "https://www.imabi.net/veteranii.htm"]

from collections import namedtuple
TitleLink = namedtuple('TitleLink', 'title link')#, defaults=(None,))


def defineOrderedFilename(number, link):
        return str(number).zfill(3) + findUrlId(link) + ".html"


def getFilesInDirectory(getPath="."):
        return [file for file in os.listdir(getPath) if os.path.isfile(getPath + "/" + file)]

def findUrlId(url):
        import re
        urlIdRegexp = re.compile(r"""https?:\/\/www.imabi.net\/([a-z0-9]*)\.html?""")
        return re.search(urlIdRegexp, url).group(1)


def getLocalSoup(filename):
    return bs.BeautifulSoup(open(filename), 'html.parser')

def getSoup(url):
	# site = 'https://dictionary.goo.ne.jp/jn/'
	# hdr = {'User-Agent': 'Mozilla/5.0'}
	print("Getting: " + url)
	hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 Chrome/41.0.2228.0 Safari/537.3'}
	req = Request(url=url, headers=hdr)
	page = urlopen(req)
	soup = bs.BeautifulSoup(page, 'lxml')
	return soup

def saveWebPage(url, filename):
        userAgent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

        headers={'User-Agent': userAgent,} 

        request=urllib.request.Request(url, None, headers) 
        response = urllib.request.urlopen(request)
        data = response.read() 
        f = open(filename, 'w')
        f.write(str(data))
        f.close()

        # sleep so the servers don't get annoyed
        sleepTime = 30 + int(random.random() * 60)
        print("sleeping for " + str(sleepTime) + " seconds.")
        time.sleep(sleepTime)


def findText(soup):
    return soup.find("div", {"id" : "fw-mainColumn"})
def findParagraphs(soup):
        return soup.find('div', {'id' : 'fw-mainColumn'}) .find_all('p')

def findSectionLinks(paragraphs):
        return [paragraph.a.get('href') for paragraph in paragraphs if paragraph.a]


def getFoldersInDirectory():
        return [folder for folder in os.listdir() if os.path.isdir(folder)]




def reNumber(string):
        import re
        findNumber = r"""[0-9]{1,3}"""
        return re.search(findNumber, string).group(1).zfill(3)

def removeEmptyLines(text):
        import re
        return re.sub(r"""\\t|\\n""", "", text)

def removeBackslashes(text):
        import re
        return re.sub(r"""\\""", "", text)


def convertHtmlToPdf(inputFile, outputFile):
        import subprocess
        subprocess.call(("weasyprint " + inputFile + " " + outputFile).split())
        
        
        
        
    
