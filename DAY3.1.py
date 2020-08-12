from selenium import webdriver 
# instagram  profile pic downloader
cd='D:\\isb superbrain\\warmupday3\\chromedriver.exe'
#open google
driver = webdriver.Chrome(cd) 

user_h=input("Enter the user handle of the profile: ")
url='https://www.instagram.com/'
url_p=url+user_h

#open the profile
driver.get(url_p)


try:
	image=driver.find_element_by_xpath('//img[@class="_6q-tv"]') # for open
except:
	image=driver.find_element_by_xpath('//img[@class="be6sR"]') # for private profile


img_link=image.get_attribute('src')


path="D:\\"+user_h+".jpg" #path where we want to store it

import urllib.request

urllib.request.urlretrieve(img_link,path) #donwloading the pic

print("The profile pic has been downloaded at: "+path)