from pprint import pprint

import pandas as pd
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plt

from aquire import get_articles()

from prepare import basic_clean, lemmatize