from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup 
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(chrome_options=chrome_options)
# import pandas as pd


options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
#C:\Users\shama\Downloads\chromedriver_win32

def getNba(team):
    # url ="https://www.nba.com/news"
    url = "https://sports.yahoo.com/nba/"
    if team is not None:
        url+="teams/"+team
    # url = 'https://sportspyder.com/nba/'+'denver-nuggets'+'/news'

    # url = 'https://www.si.com/nba/'+"celtics"+'/'
    # req= requests.get(url,timeout=(None,70))

    driver.get(url)
    time.sleep(1)
    # articles=driver.find_elements(By.XPATH,'//div[@class="Cf"]')
    articles=driver.find_elements(By.XPATH,"//h3[@class='Mb(5px)']")
    bodies=driver.find_elements(By.XPATH,"//p[@class='Fz(14px) Lh(19px) Fz(13px)--sm1024 Lh(17px)--sm1024 LineClamp(2,38px) LineClamp(2,34px)--sm1024 M(0)']")
    images=driver.find_elements(By.XPATH,"//div[@class='H(0) Ov(h) Bdrs(2px)']//img")
    sources=driver.find_elements(By.XPATH,"//div[@class='C(#959595) Fz(11px) D(ib) Mb(6px)']")
    # links=driver.find_elements(By.XPATH,"//a[@class='js-content-viewer Fw(b) Fz(18px) Lh(21px) LineClamp(2,40px) Fz(16px)!--sm1024 Lh(17px)--sm1024 LineClamp(2,34px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled wafer-destroyed']")
    links=driver.find_elements(By.XPATH,"//h3[@class='Mb(5px)']//a")

    a=[]
    for i in range(len(articles)):
        # i.append(a.find_element(By.XPATH,"//h3[@class='Mb(5px)']").text)
        try:
            heading=articles[i].text
        except Exception as e:
            heading=str(e)

        try:
            body=bodies[i].text
        except Exception as e:
            body=str(e)
        
        try:
            image=images[i].get_attribute("src")
        except Exception as e:
            image=str(e)

        try:
            link=links[i].get_attribute("href")
        except Exception as e:
            link=str(e)

        try:
            source=sources[i].text
        except Exception as e:
            source=str(e)

       
        a.append({
            'title':heading,
            'summary':body,
            'src':image,
            'link':link,
            'source':source
        })
       
           
        
    # soup=BeautifulSoup(req.content)
    # articles=soup.findAll('article')
    # articles=soup.find_all('div',class_='l-grid--item')
    # return articles
    return a




@api_view(['GET','PUT'])
def getNbaTeam(request,team):
    stories=getNba(team)
    return Response(stories)



def getNbaNews(request):
    articles=getNba()
    
    srml=""
    i=[]
    # for a in articles:
    #     # a.find('h2')
    #     i=a.find('img',class_='VideoThumbnail_image__3nEOl')
    #     if i is not None:
    #         srml+=i['src']
        
    #     t=a.find('h2',class_='t1')
    #     if t is not None:
    #         srml+='<h2>'+t.text+'</h2>'

    #     s=a.find('p',class_='t6 pt-2')
    #     if s is not None:
    #         srml+='<h4>'+s.text+'</h4>'
    print(articles is not None)
    print(articles)
    return HttpResponse(articles)

@api_view(['GET','PUT'])
def getStories(request):
    stories=[]
    
    articles=getNba()
    
    for a in articles:
        l=a.find('a')
        if l is not None:
            link=l['href']
        else: link=None
        i=a.find('img',class_='VideoThumbnail_image__3nEOl')
        if i is not None:
            img=i['src']
        else: img= None
        
        t=a.find('h2',class_='t1')
        if t is not None:
            title=t.text
        else: title= None

        s=a.find('p',class_='t6 pt-2')
        if s is not None:
            body=s.text
        else: body= None
        stories.append({
            'src':img,
            'title':title,
            'summary':body,
            'link':link,
            'source':'NBA.com'
        })
    return Response(stories)
    
        
    # story=Story(github_user=github_user,username=username,imagelink=profile)
    # github.save()


    # r = requests.get("https://www.hindustantimes.com/india-news/")
    # soup = BeautifulSoup(r.content, 'html5lib')
    # newsDivs = soup.findAll("div", {"class": "headingfour"})

