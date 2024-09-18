# web scraping script

# Making a GET request
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

#from urllib import urlopen

"""
text = urlopen('https://commonlyusedwords.com/2000-most-common-Spanish-words/').read()
soup = BeautifulSoup(text)
#print(soup)
spanish = soup.select('td')
"""

def has_td_siblings(x):
    return x.find_next_sibling().name == 'td'

r = requests.get('https://commonlyusedwords.com/2000-most-common-Spanish-words/')
soup = bs(r.text, 'html.parser')

spanish_vocab = soup.select('tbody')

for element in spanish_vocab:
    if has_td_siblings(element):
        print('yes')
    else: 
        print ('no')



 





