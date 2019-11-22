#drum and bass makes coding much cooler

from __future__ import division
import itertools
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import math
from sklearn import metrics
from random import randint
from matplotlib import style
import seaborn as sns

# Use basic probability to identify anomalous request methods. 
# You will want to make sure the text is normalized in order to reduce the noise.