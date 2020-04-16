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

# 防止Mac中文乱码问题
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

#显示所有列
#pd.set_option('display.max_columns', None)
#显示所有行
#pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
#pd.set_option('max_colwidth',100)
