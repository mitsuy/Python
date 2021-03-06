'''
   Scraping test by Python3.

   How to extract main and flash news items from 
  Mainichi news site.

 Written by M.Yagyu, 12 Sep. 2019 

'''
# -- coding : utf-8 --#


import urllib.request,urllib.error
from bs4 import BeautifulSoup
import csv


##############################
##   Main news items        ## 
##############################

# URL accessed
url="https://mainichi.jp/"

# Open URL
html=urllib.request.urlopen(url)
#Open by BS
soup=BeautifulSoup(html,"html.parser")

# Narrow a tag used for news viewing from HTML
tag_mainbox=soup.select_one(".main-box")
tag_listA=tag_mainbox.select_one(".list-typeA")
news_tag=tag_listA.findAll("a")

# Open the csv file. if there not, make file
f=open("main_news.csv","w",encoding="utf_8_sig")
write_main=csv.writer(f)

# Make array.
mainlist=["# Main News"]

# Output
write_main.writerow(mainlist)

it=0
for news_txt in news_tag:
    news_txt=news_txt.text
    mainlist=[it+1,news_txt]

    # Output
    write_main.writerow(mainlist)
    it=it+1
#end for

# Close csv file.
f.close()


##############################
##   Flash news items       ## 
##############################

# URL
url_flash="https://mainichi.jp/flash/1"

html_flash=urllib.request.urlopen(url_flash)
soup_flash=BeautifulSoup(html_flash,"html.parser")


list_sub=soup_flash.select_one(".list-typeA")
list_midashi=list_sub.select(".midashi")
list_date=list_sub.select(".date")
list=list_sub.select("a")
#print(list_midashi[0].text)

g=open("flash_news.csv","w",encoding="utf_8_sig")
write_sub=csv.writer(g)
sublist=["# Flash news"]

write_sub.writerow(sublist)

i=0
for sub_txt in list:

    sublist_midashi=[i+1 ,list_midashi[i].text]
    sublist_date=["",list_date[i].text]
    
    # Output
    write_sub.writerow(sublist_midashi)
    write_sub.writerow(sublist_date)
    
    i=i+1
#end for

g.close()
