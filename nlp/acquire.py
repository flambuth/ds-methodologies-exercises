#I want to be a cowboy. I'm going to be a cowboy. A cowboy!

import requests
import pandas as pd
from bs4 import BeautifulSoup

# Codeup Blog Articles

# Scrape the article text from the following pages:

# https://codeup.com/codeups-data-science-career-accelerator-is-here/
# https://codeup.com/data-science-myths/
# https://codeup.com/data-science-vs-data-analytics-whats-the-difference/
# https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/
# https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/

def get_blog_articles():
    pass

#That parameter was created by using the Inspet Element on the page. Right clicking on the element brings up the 
#option to Copy Selctor. Then paste that inside the (). Makes an iterable. The [0] index has a method that cuts
#off the HTML and just gives you a string.
soup.select(".mk-single-content > p:nth-child(1)")[0].get_text() 