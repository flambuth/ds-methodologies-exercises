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

def stem():
    """
    accept some text and return the text after applying stemming to all the words.
    """
    pass

def lemmatize():
    """
    accept some text and return the text after applying lemmatization to each word.
    """
    pass

def remove_stopwords():
    """
    accept some text and return the text after removing all the stopwords.
    """
    pass 

def prepare_text():
    """
    Do all the prior functions to a corpus.
    """
    pass