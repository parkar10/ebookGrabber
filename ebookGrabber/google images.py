import requests
from bs4 import BeautifulSoup

def images(name):
    list = name.split(" ")

    name = ""
    for x in list:
        name = name+"+"+x
    name = name[1:len(name)]

    gurl = "https://www.google.co.in/search?q="+name+"&hl=en&authuser=0&tbm=isch&source=lnt&tbs=isz:l&sa=X&ved=0ahUKEwil7r_r5PfaAhUBMo8KHS99AJgQpwUIHw&biw=1440&bih=769&dpr=1"
    print(gurl)
    sc = requests.get(gurl)
    pt = sc.text
    #print(pt)
    list = []
    soup = BeautifulSoup(pt, "html.parser")
    for link in soup.findAll('img',{"class":"rg_ic rg_i"}):
        hrefs = link.get('src')
        if 'yahoo' not in hrefs:
            list.append(hrefs)
            print(hrefs)


    print(list)


images("akshay parkar")