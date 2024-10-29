import requests
from bs4 import BeautifulSoup



qheader={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

burl='https://books.toscrape.com/'
qresp=requests.get(url=burl,headers=qheader)

qsoup=BeautifulSoup(qresp.content,'html.parser')


books_data={}
titles=qsoup.findAll('a',title=True)
prices=qsoup.findAll('p',attrs={'class':'price-color'})
ratings=qsoup.findAll('p',attrs={'class':'star-rating'})
for i in range(len(titles)):
    title=titles[i]['title']
    #price=prices[i]['class']
    rating=ratings[i]['class']
    
    books_data={
        'title':title,
        #'price':price,
        'rating':rating
    }
    print('books_data',books_data)
    #books_data.append(books_data)
    
    
