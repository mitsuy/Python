import requests
from bs4 import BeautifulSoup


def main():

    url="https://news.yahoo.co.jp/topics"
    
    #html="<h1>sayhello</h1>,<h1>saysay</h1>,<h2>say</h2>"
    r=requests.get(url)
    print(r.status_code)
    soup=BeautifulSoup(r.content,"html.parser")

    #print(soup.find("div",id="contentsWrap").text)

#end main


if __name__=='__main__':
    main()
