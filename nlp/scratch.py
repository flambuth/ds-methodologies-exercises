pageX = requests.get('https://codeup.com/codeups-data-science-career-accelerator-is-here/', headers=headers)  

soup = BeautifulSoup(pageX.content, 'html.parser')


#That parameter was created by using the Inspet Element on the page. Right clicking on the element brings up the 
#option to Copy Selctor. Then paste that inside the (). Makes an iterable. The [0] index has a method that cuts
#off the HTML and just gives you a string.
soup.select(".mk-single-content > p:nth-child(1)")[0].get_text() 

#Broadened the search
page1_text = soup.select(".mk-single-content")[0].get_text()                 

#I"M SO DRUNK! Still coding.
laFleur = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
type(laFleur)
sopa = BeautifulSoup(laFleur.content, 'html.parser')
sopa
sopa.find_all('p')
laFleur = requests.get("https://codeup.com/data-science-myths/")
sopa = BeautifulSoup(laFleur.content, 'html.parser')
sopa
headers = {'User-Agent': 'Codeup Bayes Data Science'}
laFleur = requests.get("https://codeup.com/data-science-myths/", headers=headers)
sopa = BeautifulSoup(laFleur.content, 'html.parser')
sopa
sopa.find_all('p')

#THE GOLDEN GOOSE!
for i in sopa.find_all('p'): 
    ...:     print(i.get_text()) 

#This might bear fruit
sopa.find_all('p', class_='mk-single-content')  

#Another fruit possiblity
#Has more than just the content from the golden goose
sopa.find_all(id="954").get_text() 


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

headers = {'User-Agent': 'Codeup Bayes Data Science'}
laFleur = requests.get("https://codeup.com/data-science-myths/", headers=headers)
sopa = BeautifulSoup(laFleur.content, 'html.parser')
sopa
sopa.find_all('p')

#THE GOLDEN GOOSE!
for i in sopa.find_all('p'): 
    ...:     print(i.get_text()) 

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
    headers = {'User-Agent': 'Codeup Bayes Data Science'} 
    response = requests.get(url, headers=headers)
    sopa = BeautifulSoup(response.content, 'html.parser')
    content = sopa.select("div.mk-single-content.clearfix")[0].get_text()
    title = sopa.title.string
    a = {'Title': title, 'Content': content}
    return a

def get_blog_posts():
    filename = './codeup_blog_posts.csv'

    # check for presence of the file or make a new request
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        return make_new_request()

def get_news_articles():
    categories = ['Business', 'Sports', 'Technology', 'Entertainment']
    #OUTER LOOP is going through the 4 categories. They're attached at the end of the URL.
    
    list_of_dicts = []
    
    for category in categories:
        #The response will grab as many articles that are loaded when hitting the URL
        headers = {'user-agent': 'Fred'}
        response = requests.get(f'https://inshorts.com/en/read/{category}', headers=headers).text
        soup = BeautifulSoup(response, 'html.parser')

        #The div class news-card holds all the information we want.
        articles = soup.select('.news-card')

        #Inner loops, (within the outer loop of Category) will find the class inside the news-card div.
        for article in articles: 
            #We grab the first [0] appearance of each of the tags we're selecting. Assigning each to a variable.
            title = article.select("[itemprop='headline']")[0].get_text()
            content = article.select("[itemprop='articleBody']")[0].get_text()
            author = article.select(".author")[0].get_text()
            published_date = article.select(".time")[0]["content"]
            category = category
            #Those string variables will each become a value in a dictionary. 
            article_data = {
                'title': title,
                'content': content,
                'category': category,
                'author': author,
                'published_date': published_date,
            }
            #Each dictonary made in the INNER LOOP gets appended.
            list_of_dicts.append(article_data)

    #That list we were making down at the INNER LOOP level. Thats the final product 
    return list_of_dicts

def get_articles_from_topic(url):
    headers = {'user-agent': 'Codeup Bayes Instructor Example'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    output = []

    articles = soup.select(".news-card")

    for article in articles: 
        title = article.select("[itemprop='headline']")[0].get_text()
        content = article.select("[itemprop='articleBody']")[0].get_text()
        author = article.select(".author")[0].get_text()
        published_date = article.select(".time")[0]["content"]
        category = response.url.split("/")[-1]

        article_data = {
            'title': title,
            'content': content,
            'category': category,
            'author': author,
            'published_date': published_date,
        }
        output.append(article_data)


    return output

def get_articles_by_category():
    categories = ['business', 'sports', 'technology', 'entertainment']
    headers = {'user-agent': 'Codeup Bayes Instructor Example'}
    output = []
    for category in categories:
        response = requests.get(f"https://inshorts.com/en/read/{category}", headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = soup.select(".news-card")

        for article in articles: 
            title = article.select("[itemprop='headline']")[0].get_text()
            content = article.select("[itemprop='articleBody']")[0].get_text()
            author = article.select(".author")[0].get_text()
            published_date = article.select(".time")[0]["content"]
            category = category

            article_data = {
                'title': title,
                'content': content,
                'category': category,
                'author': author,
                'published_date': published_date,
            }
            output.append(article_data)

    return output



def basic_clean(text):
    """
    Lowercase everything
    Normalize unicode characters
    Replace anything that is not a letter, number, whitespace or a single quote.
    """
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    text = re.sub(r"[^a-z0-9'\s]", '', text)
    return text 


long_string = "The rumors are true! The time has arrived. Codeup has officially opened applications to our new Data Science career accelerator, with only 25 seats available! This immersive program is one of a kind in San Antonio, and will help you land a job in Glassdoor’s #1 Best Job in America. Data Science is a method of providing actionable intelligence from data. The data revolution has hit San Antonio, resulting in an explosion in Data Scientist positions across companies like USAA, Accenture, Booz Allen Hamilton, and HEB. We’ve even seen UTSA invest $70 M for a Cybersecurity Center and School of Data Science. We built a program to specifically meet the growing demands of this industry. Our program will be 18 weeks long, full-time, hands-on, and project-based. Our curriculum development and instruction is led by Senior Data Scientist, Maggie Giust, who has worked at HEB, Capital Group, and Rackspace, along with input from dozens of practitioners and hiring partners. Students will work with real data sets, realistic problems, and the entire data science pipeline from collection to deployment. They will receive professional development training in resume writing, interviewing, and continuing education to prepare for a smooth transition to the workforce. We focus on applied data science for immediate impact and ROI in a business, which is how we can back it all up with a 6 month tuition refund guarantee – just like our existing Web Dev program. We’re focusing on Data Science with Python, SQL, and ML, covered in 14 modules: 1) Fundamentals; 2) Applied statistics; 3) SQL; 4) Python; 5) Supervised machine learning – regression; 6) Supervised machine learning – classification; 7) Unsupervised machine learning – clustering; 8) Time series analysis; 9) Anomaly detection; 10) Natural language processing; 11) Distributed machine learning; 12) Advanced topics (deep learning, NoSQL, cloud deployment, etc.); 13) Storytelling with data; and 14) Domain expertise development. Applications are now open for Codeup’s first Data Science cohort, which will start class on February 4, 2019. Hurry – there are only 25 seats available! To further our mission of cultivating inclusive growth, scholarships will be available to women, minorities, LGBTQIA+ individuals, veterans, first responders, and people relocating to San Antonio. If you want to learn about joining our program or hiring our graduates, email datascience@codeup.com!"



def tokenize(text):
    """
    take in a string and tokenize all the words in the string.
    """
    tokenizer = nltk.tokenize.ToktokTokenizer()
    return tokenizer.tokenize(text, return_str=True)


def stem(text):
    """
    accept some text and return the text after applying stemming to all the words.
    """
    ps = nltk.porter.PorterStemmer()

    stems = [ps.stem(word) for word in text.split()]
    article_stemmed = ' '.join(stems)
    return article_stemmed

def lemmatize(text):
    """
    accept some text and return the text after applying lemmatization to each word.
    """
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in text.split()]
    return ' '.join(lemmas)

wnl = nltk.stem.WordNetLemmatizer()

for word in 'study studies'.split():
    print('stem:', ps.stem(word), '-- lemma:', wnl.lemmatize(word))

lemmas = [wnl.lemmatize(word) for word in article.split()]
article_lemmatized = ' '.join(lemmas)

print(article_lemmatized)