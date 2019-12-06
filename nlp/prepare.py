#I can break it down like this. 

import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd

import acquire

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

def remove_stopwords(text):
    """
    accept some text and return the text after removing all the stopwords.
    """
    stopword_list = stopwords.words('english')
    words = text.split()
    filtered_words = [w for w in words if w not in stopword_list]
    return ' '.join(filtered_words)

def prepare_text(art_dict):
    """
    takes in the dictionary representing an article and returns a dictionary that looks like this:
    {
    'title': 'the original title'.
    'original': original,
    'stemmed': article_stemmed,
    'lemmatized': article_lemmatized,
    'clean': article_without_stopwords
    }
    """
    art_dict['Content'] = basic_clean(art_dict['Content'])

    prepped_dict = {
    'title' : art_dict['Title'],
    'original' : art_dict['Content'],
    'stemmed' : stem(art_dict['Content']),
    'lemmatized' : lemmatize(art_dict['Content']),
    'clean' : remove_stopwords(art_dict['Content'])
    }
    return prepped_dict