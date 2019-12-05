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

def get_codeup_webcontent(url):
    """
    Returns a 2Key Dictionary that is a string for ['Title'] and a list for ['Content']
    """
    content = []
    headers = {'User-Agent': 'Codeup Bayes Data Science'} 
    response = requests.get(url, headers=headers)
    sopa = BeautifulSoup(response.content, 'html.parser')
    for i in sopa.find_all('p'):
        #print(i.get_text())
        content.append(i.get_text())
    title = sopa.select('title')[0].get_text()
    a = {'Title': title, 'Content': content}
    return a


def make_dict_of_web_content():
    """
    Returns a list of dictionaries. Each dictionary is one created from the prior function. 
    I need to fix it so that each list element has a unique name
    """
    urls = [
    "https://codeup.com/codeups-data-science-career-accelerator-is-here/",
    "https://codeup.com/data-science-myths/",
    "https://codeup.com/data-science-vs-data-analytics-whats-the-difference/",
    "https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/",
    "https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/"
    ]
    pages = []

    for i in urls:
        page = get_codeup_webcontent(i)
        pages.append(page)
    return pages

