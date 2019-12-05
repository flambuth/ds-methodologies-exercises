#I want to be a cowboy. I'm going to be a cowboy. A cowboy!

import requests
import pandas as pd
from bs4 import BeautifulSoup

# Codeup Blog Articles

# Scrape the article text from the following pages:
urls = [
"https://codeup.com/codeups-data-science-career-accelerator-is-here/",
"https://codeup.com/data-science-myths/",
"https://codeup.com/data-science-vs-data-analytics-whats-the-difference/",
"https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/",
"https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/"
]
# #The header will avoid that 403 error
# url = 'https://codeup.com/codeups-data-science-career-accelerator-is-here/'
# headers = {'User-Agent': 'Codeup Bayes Data Science'} # codeup.com doesn't like our default user-agent
# response = get(url, headers=headers)

def get_blog_articles():
    url = 'https://codeup.com/codeups-data-science-career-accelerator-is-here/'
    headers = {'User-Agent': 'Codeup Bayes Data Science'} # codeup.com doesn't like our default user-agent
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    page1_text = soup.select(".mk-single-content")[0].get_text()
    return page1_text

def get_stuff(url):
    headers = {'User-Agent': 'Codeup Bayes Data Science'} # codeup.com doesn't like our default user-agent
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    page1_text = soup.select(".mk-single-content")[0].get_text()
    return page1_text


def get_codeup_webcontent(url):
    content = []
    headers = {'User-Agent': 'Codeup Bayes Data Science'} 
    response = requests.get(url, headers=headers)
    sopa = sopa = BeautifulSoup(response.content, 'html.parser')
    for i in sopa.find_all('p'):
        #print(i.get_text())
        content.append(i.get_text())
    title = sopa.select('title')[0].get_text()
    return title, content
#Returns a List. Each list element is a <p> element.

def make_dict_of_web_content():
    #List of Dictionaries, so each element will be a DICT with 2 keys(title, content)
    pages = []
    #Each step of the loop will generate a 2-Key-DICT, then appended to the pages list 
    for i in urls:
        get_codeup_webcontent(i)

    
    pass

headers = {'User-Agent': 'Codeup Bayes Data Science'}
laFleur = requests.get("https://codeup.com/data-science-myths/", headers=headers)
sopa = BeautifulSoup(laFleur.content, 'html.parser')
sopa
sopa.find_all('p')

#THE GOLDEN GOOSE!
for i in sopa.find_all('p'): 
    ...:     print(i.get_text()) 