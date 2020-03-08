# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:05:35 2020

@author: Anirudh Raghavan
"""

import requests as req
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        tmp = str(data)
        if tmp[0] == 'N':
            return names.append(tmp)
        elif tmp[0] == 'P':
            return purposes.append(tmp)
    
#Source:https://docs.python.org/3.4/library/html.parser.html

def my_scraper (a):
    for i in range(a):
        get_resp = req.get('http://18.207.92.139:8000/random_company')
        parser = MyHTMLParser()
        parser.feed(get_resp.text)


if __name__ == "__main__":
    file1 = open(r"C:\Users\Anirudh Raghavan\Desktop\Stevens - Courses\Spring 2020\FE 595 - FinTech\Assignments\Company Details",
             "w") 
    file1.write("Company Details \n")
    file1.close()
    
    names = []
    purposes = []
    my_scraper(50)
    
    file1 = open(r"C:\Users\Anirudh Raghavan\Desktop\Stevens - Courses\Spring 2020\FE 595 - FinTech\Assignments\Company Details",
             "a") 
    for i in range(len(names)):
        name = names[i] + "\n" 
        file1.write(name)
        purpose = purposes[i] + "\n"
        file1.write(purpose)
        file1.close()
    file1.close()



