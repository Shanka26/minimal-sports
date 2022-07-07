from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup 
from rest_framework.response import Response
from rest_framework.decorators import api_view


def getNba():
    url ="https://www.nba.com/news"
    req=requests.get(url)
    soup=BeautifulSoup(req.content)
    articles=soup.findAll('article')
    return articles

def getNbaNews(request):
    articles=getNba()
    srml=""
    for a in articles:
        # a.find('h2')
        srml+="<img src="+str(a.find('img'))+"/>"
        srml+='<h2>'+str(a.find('h2'))+'</h2>'
        srml+='<h4>'+str(a.find('p'))+'</h4>'
    
    return HttpResponse(srml)

@api_view(['GET','PUT'])
def getStories(request):
    stories=[]
    
    articles=getNba()
    
    for a in articles:
        img=str(a.find('img'))
        title=str(a.find('h2'))
        body=str(a.find('p'))
        stories.append({
            'src':img,
            'title':title,
            'summary':body
        })
    return Response(stories)
    
        
    # story=Story(github_user=github_user,username=username,imagelink=profile)
    # github.save()


    # r = requests.get("https://www.hindustantimes.com/india-news/")
    # soup = BeautifulSoup(r.content, 'html5lib')
    # newsDivs = soup.findAll("div", {"class": "headingfour"})

