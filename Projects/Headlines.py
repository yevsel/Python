import requests
from bs4 import BeautifulSoup

page=requests.get('https://www.myjoyonline.com/')

soup=BeautifulSoup(page.content,'html.parser')

now=soup.find_all(class_='col-lg-6 col-sm-6 col-md-6 col-xs-12 mt-3')

today=[i.find(class_='col-xs-6 col-md-6 col-sm-6 nopadding img-holder') for i in now]

todaylink=[i.find('a')['href'] for i in today]

todaycaption=[i.find('h4').text for i in now]

top=soup.find(class_='title-summary position-absolute dark-gradient p-3').text.strip()


print('T O P    N E W S')
print()
print(top,'\n'*3)


print('T O D A Y S      N E W S')
print()
for i in todaycaption:
    print(i,'\n')


x=input('DONE')
