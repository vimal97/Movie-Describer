import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from bs4 import BeautifulSoup

from urllib.request import Request, urlopen

film=input("Enter the name of film : ")

#modified google search query
url="https://www.google.com/search?q="+film

#open the url after specifyin the user agent
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()

soup = BeautifulSoup(html, 'lxml')
div=[]


metadata=soup.find_all(class_="V7Q8V")
#find the imdb div having the rating value using the class name
div=soup.find_all(class_="sDYTm")

#print the results
print()
if(len(div)>0):
    print("Film name : ",film,end='\n\n')
    for j in metadata:
        print(j.get_text(),end='\n\n')
else:
    print("No results available for the given film (Check if it is spelled correctly and run the program again.. :)")