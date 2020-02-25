# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:42:56 2020

@author: Anirudh Raghavan
"""

import requests as req
from html.parser import HTMLParser

file1 = open(r"C:\Users\Anirudh Raghavan\Desktop\Stevens - Courses\Spring 2020\FE 595 - FinTech\Assignments\Company Details",
             "w") 
file1.write("Company Details \n")
file1.close()

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        tmp = str(data)
        tmp = tmp + "\n"
        if tmp[0] == 'N':
            file1 = open(r"C:\Users\Anirudh Raghavan\Desktop\Stevens - Courses\Spring 2020\FE 595 - FinTech\Assignments\Company Details",
             "a")
            file1.write(tmp)
            file1.close()
        elif tmp[0] == 'P':
            file1 = open(r"C:\Users\Anirudh Raghavan\Desktop\Stevens - Courses\Spring 2020\FE 595 - FinTech\Assignments\Company Details",
             "a")
            file1.write(tmp)
            file1.close()

#Source:https://docs.python.org/3.4/library/html.parser.html

def my_scraper (a):
    for i in range(a):
        get_resp = req.get('http://18.207.92.139:8000/random_company')
        parser = MyHTMLParser()
        parser.feed(get_resp.text)

if __name__ == "__main__":
    my_scraper(50)


