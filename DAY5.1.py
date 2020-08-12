'''
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup

p=int(input('Enter the number of pages:'))

titles = []
links = []
for i in range(p):
	url='https://news.ycombinator.com/news?p='+str(i+1)
	r=urllib.request.urlopen(url)
	c=r.read()
	soup = BeautifulSoup(c,'html.parser')
	d=soup.find('table',{'class':'itemlist'}).find_all('a',{'class':'storylink'})

	for j in d:
		title=j.text 
		link=j.get('href')
		titles.append(title)
		links.append(link)

dic = {'news_title':titles,'URL':links}

df=pd.Dataframe(dic) #DataFrame

print(df)
'''
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

p=int(input("Enter the number of pages: "))


titles=[]
links=[]
for i in range(p):
	url='https://news.ycombinator.com/news?p='+str(i+1)
	r=urllib.request.urlopen(url)
	c=r.read()
	soup=BeautifulSoup(c,'html.parser')
	d=soup.find('table',{'class':'itemlist'}).find_all('a',{'class':'storylink'})

	for j in d:
		title=j.text
		link=j.get('href')
		titles.append(title)
		links.append(link)

dic={'news_title':titles,'URL':links}

df=pd.DataFrame(dic)

print(df)
df.to_csv("D:\\isb superbrain\\warmupday5\\news.csv",index=False)
print("Done")