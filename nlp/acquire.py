#I want to be a cowboy. I'm going to be a cowboy. A cowboy!

import requests
import pandas as pd
from bs4 import BeautifulSoup
import os

def get_codeup_blog_data():
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        return aquire_all_pages()

def get_codeup_page(url):
    """
    Returns a 2Key Dictionary that is a string for ['Title'] and a list for ['Content']
    """
    headers = {'User-Agent': 'Codeup Bayes Data Science'} 
    response = requests.get(url, headers=headers)
    sopa = BeautifulSoup(response.content, 'html.parser')
    content = sopa.select("div.mk-single-content.clearfix")[0].get_text()
    title = sopa.title.string
    a = {'Title': title, 'Content': content}
    return a

def aquire_all_pages():
    """
    Returns a list of dictionaries. Each dictionary is one created from the prior function. 
    I need to fix it so that each list element has a unique name
    """
    filename = './codeup_blog_posts.csv'

    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        return aquire_all_pages()
    
    urls = [
    "https://codeup.com/codeups-data-science-career-accelerator-is-here/",
    "https://codeup.com/data-science-myths/",
    "https://codeup.com/data-science-vs-data-analytics-whats-the-difference/",
    "https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/",
    "https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/"
    ]
    pages = []

    for i in urls:
        page = get_codeup_page(i)
        pages.append(page)
    
    df = pd.DataFrame(pages)

    df.to_csv('codeup_blog_posts.csv') 
    return df

#2
########
# News Articles


# Write a function that scrapes the news articles for the following topics:

# Business
# Sports
# Technology
# Entertainment
# The end product of this should be a function named get_news_articles that returns a list of dictionaries, 
# where each dictionary has this shape:
# {
#     'title': 'The article title',
#     'content': 'The article content',
#     'category': 'business' # for example
# }
news_http = requests.get('https://inshorts.com/en/read').text
soupe = BeautifulSoup(news_http, 'html.parser')

#TITLE
soupe.find('span', itemprop='headline').text 

#'CONTENT'
#Finds first paragraph of news content
soupe.find('div', class_='news-card-content news-right-box').text 


#CATEGORY
categories = ['Business', 'Sports', 'Technology', 'Entertainment']

def get_news_articles():
    categories = ['Business', 'Sports', 'Technology', 'Entertainment']
    for category in categories:
        response = requests.get(f'https://inshorts.com/en/read/{category}').text
        soup = BeautifulSoup(response, 'html.parser')
        print(f"Category: {category}")
        print(soup.find('span', itemprop='headline').text)
        print(soup.find('div', class_='news-card-content news-right-box').text)