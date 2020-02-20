import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from datetime import datetime as dt
from pylab import mpl
import glob
#from sklearn import linear_model
#import scipy.stats as scs
#import psycopg2
#from ipywidgets import interact,interactive,fixed
#import ipywidgets as widgets

%matplotlib inline
mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.style.use('ggplot')
pd.set_option('display.float_format', lambda x: '%.5f' % x)

import matplotlib as mpl
from matplotlib.font_manager import _rebuild
_rebuild()
#防止中文乱码问题

%%HTML
<button onclick="$('.input, .output_stderr, .output_error').toggle();">Toggle Code</button> 
