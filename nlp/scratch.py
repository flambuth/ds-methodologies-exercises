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