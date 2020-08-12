'''from selenium import webdriver
import time
import pandas as pd 

wb='D:\\isb superbrain\\warmupday5\\chromedriver.exe'
browser=webdriver.Chrome(wb)

browser.get('https://twitter.com/explore/tabs/trending')
time.sleep(10)
sp=browser.find_elements_by_tag_name('span')
fl=[]
for i in sp:
	a=i.get_attribute('textcontent')
	if(a.startswith('#')):
		if a not in fl:
			fl.append(a)


urls=[]
for i in fl:
	i=i[1:]
	url = 'https://twitter.com/search?q=%23GreenIndiaChallenge&src=trend_click'
	urls.append(url)

dic={'HashTag':fl,'URL':urls}

df = pd.DataFrame(dic)
'''

  
from selenium import webdriver
import time
import pandas as pd
cd='D:\\isb superbrain\\warmupday5\\chromedriver.exe'
browser=webdriver.Chrome(cd)

browser.get('https://twitter.com/explore/tabs/trending')
time.sleep(15)
sp=browser.find_elements_by_tag_name('span')
fl=[]
for i in sp:
	a=i.get_attribute('textContent')
	if (a.startswith('#')):
		if a not in fl:
			fl.append(a)

urls=[]
for i in fl:
	i=i[1:]
	url='https://twitter.com/search?q=%23'+i+'&src=trend_click'
	urls.append(url)

dic={'HashTag':fl,'URL':urls}

df=pd.DataFrame(dic)

df.to_csv('D:\\isb superbrain\\warmupday5\\twitter.csv',index=False)

print('Done')
