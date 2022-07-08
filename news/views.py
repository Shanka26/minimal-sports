from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup 
from rest_framework.response import Response
from rest_framework.decorators import api_view


def getNba():
    # url ="https://www.nba.com/news"
    url ="https://sports.yahoo.com/nba/teams/"+'boston'
    req=requests.get(url)
    soup=BeautifulSoup(req.content)
    # articles=soup.findAll('article')
    articles=soup.findAll('div',class_='Cf')
    return articles


@api_view(['GET','PUT'])
def getNbaTeam(request,team):
    url ="https://sports.yahoo.com/nba/teams/"+team
    req=requests.get(url)
    soup=BeautifulSoup(req.content)
    stories=[]
    articles=soup.findAll('div',class_='Cf')
    for a in articles:
        l=a.find('a',class_='js-content-viewer Fw(b) Fz(18px) Lh(21px) LineClamp(2,40px) Fz(16px)!--sm1024 Lh(17px)--sm1024 LineClamp(2,34px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled wafer-destroyed')
        if l is not None:
            link=l['href']
        else: link=None

        i=a.find('img',class_='W(100%) Trsdu(0s)! Bdrs(2px)')
        if i is not None:
            img=i['src']
        else: img= None

        c=a.find('div',class_='C(#959595) Fz(11px) D(ib) Mb(6px)').find('span')
        if c is not None:
            source=c.text
        else: source= None
        
        t=a.find('h3',class_='Mb(5px)')
        if t is not None:
            title=t.text
        else: title= None

        s=a.find('p',class_='Fz(14px) Lh(19px) Fz(13px)--sm1024 Lh(17px)--sm1024 LineClamp(2,38px) LineClamp(2,34px)--sm1024 M(0)')
        if s is not None:
            body=s.text
        else: body= None

        stories.append({
            'src':img,
            'title':title,
            'summary':body,
            'link':link,
            'source':source
        })
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

