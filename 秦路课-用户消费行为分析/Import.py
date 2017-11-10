import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime as dt
from pylab import mpl 

%matplotlib inline
mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.style.use('ggplot')

%%HTML
<button onclick="$('.input, .output_stderr, .output_error, .output_result').toggle();">Toggle Code</button>
#[1]:.prompt, 去掉前面的编号 
