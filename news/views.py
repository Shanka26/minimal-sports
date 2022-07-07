from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup 



def getNbaNews(request):

    url ="https://www.nba.com/news"
    req=requests.get(url)
    soup=BeautifulSoup(req.content)
    articles=soup.findAll('article')
    stories={}
    srml=""
    for a in articles:
        # a.find('h2')
        srml+="<img src="+str(a.find('img'))+"/>"
        srml+='<h2>'+str(a.find('h2'))+'</h2>'
        srml+='<h4>'+str(a.find('p'))+'</h4>'
        
    tpe = type(articles)
    
    return HttpResponse(srml)
    # story=Story(github_user=github_user,username=username,imagelink=profile)
    # github.save()


    # r = requests.get("https://www.hindustantimes.com/india-news/")
    # soup = BeautifulSoup(r.content, 'html5lib')
    # newsDivs = soup.findAll("div", {"class": "headingfour"})

