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
    i=[]
    for a in articles:
        # a.find('h2')
        i=a.find('img',class_='VideoThumbnail_image__3nEOl')
        if i is not None:
            srml+=i['src']
        
        t=a.find('h2',class_='t1')
        if t is not None:
            srml+='<h2>'+t.text+'</h2>'

        s=a.find('p',class_='t6 pt-2')
        if s is not None:
            srml+='<h4>'+s.text+'</h4>'
    
    return HttpResponse(srml)

@api_view(['GET','PUT'])
def getStories(request):
    stories=[]
    
    articles=getNba()
    
    for a in articles:
        i=a.find('img',class_='VideoThumbnail_image__3nEOl')
        if i is not None:
            img=i['src']
        
        t=a.find('h2',class_='t1')
        if t is not None:
            title='<h2>'+t.text+'</h2>'

        s=a.find('p',class_='t6 pt-2')
        if s is not None:
            body='<h4>'+s.text+'</h4>'
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

