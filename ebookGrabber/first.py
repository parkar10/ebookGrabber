import requests
from bs4 import BeautifulSoup

def ebooks(name):
    list = name.split(" ")

    name = ""
    for x in list:
        name = name+"+"+x
    name = name[1:len(name)]

    yurl = "https://in.search.yahoo.com/search?p="+name+"+filetype%3Apdf&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8"
    print(yurl)
    sc = requests.get(yurl)
    pt = sc.text
    #print(pt)
    list = []
    soup = BeautifulSoup(pt, "html.parser")
    for link in soup.findAll('a',{"class":"td-u"}):
        hrefs = link.get('href')
        if 'yahoo' not in hrefs:
            list.append(hrefs)
            print(hrefs)


    print(list)








ebooks("r s aggarwal quantitative aptitude")

