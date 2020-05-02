# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:24:59 2020

@author: Randhirs
"""
import requests
from bs4 import BeautifulSoup 
import csv
import os

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL).text 

soup = BeautifulSoup(r, 'lxml')

#print(soup.prettify())


quotes_text = []
quotes_image =[]
quotes_url =[]
quotes_url_final = []
url_string = "https://www.passiton.com"

# We nee to write in a csv file
csv_file = open('quotes_details_final.csv', 'w')
csv_writer =csv.writer(csv_file)
csv_writer.writerow(['quotes', 'image_url', 'quotes_url'])

for all_quotes in soup.find_all('div', class_ ='col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top') :
    
    
    
    for image in all_quotes.find_all('img') :
        #print("Adding quotes to the list")
        quotes_text.append(image['alt'])
        # print("Adding url to the list")
        quotes_image.append(image['src'])
        
    # Grabing all href from    all_quotes
    for url in all_quotes.find_all('a', href=True) :
        quotes_url.append(url_string+str(url).split('href')[1].split('">')[0].split('"')[1])
        #url_string+str(url).split('href')[1].split('">')[0].split('"')[1]
        #print("HI")
        

    #for quotes in quotes_url :
        #quotes_url_final.append(url_string+str(quotes).split('href')[1].split('">')[0].split('"')[1])
         #quotes_url_final = url_string+str(quotes).split('href')[1].split('">')[0].split('"')[1]
        # Removing duplicates from a list quotes_url_final , using dict
    
    quotes_url_final = list(dict.fromkeys(quotes_url_final))

    csv_writer.writerow([image['alt'], image['src'], url_string+str(url).split('href')[1].split('">')[0].split('"')[1]])

csv_file.close()
#os.remove("quotes_details.csv")



