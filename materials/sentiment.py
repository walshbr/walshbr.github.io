from bs4 import BeautifulSoup
from urllib import request
import nltk
from textblob import TextBlob
from matplotlib import pyplot as plt

# scrape the text
url = 'http://walshbr.com/materials/sentiment.txt'
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')
raw_text = soup.text
print(raw_text)

# turn it into sentences
blob = TextBlob(raw_text)

polarities = []
for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
    polarities.append(sentence.sentiment.polarity)
    
#
print(polarities)
# do some text blob stuff to it
# to graph it they'll need to give it x coordinates

plt.plot(polarities)
plt.show() 