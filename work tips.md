# pandas
1. [生成时间序列](https://blog.csdn.net/you_are_my_dream/article/details/70209757)  
    [对时间序列重新采样](https://blog.csdn.net/wangshuang1631/article/details/52314944)  
    
    `pd.date_range(start, end, freq, tz, closed)`  
    `DataFrame.resample()`
    `拆解时间序列: date.apply(lambda date:date.year/month/day)`  
  
2. 由于pandas和python特性，避免io读取和for循环以提高获取数据速度
     - read_sql 改为 read_csv，本地读取百万级以上的数据  
     - pd.read_csv(chunk_size=100)可大幅提高读写速度(300万条数据4分钟),但是读取的数据是generator      
     - [重要][优化代码执行速度](https://python.freelycode.com/contribution/detail/1083)  ：采用apply或向量化

3. [熟练使用交互可视化](http://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html)

    `import ipywidgets as widgets`
    
4. 行列操作  

    `df.loc[:,:]=value`行  
    `df[columns]=value`列  
    `df.apply(lambda x:x.idxmax(), axis=1)`极值行列  
    `df.reindex() df.rename()` 修改行   
    
 
5. [利用glob/os.path合并多个csv文件](https://blog.csdn.net/u010129985/article/details/79177359)  

6. apply用于df行列，applymap用于df元素;map用于series和一个函数或字典型对象

7. 读取txt:read_table

8. 连续数据用分布概率函数，离散数据用概率密度函数

9. eval()函数执行字符串格式的表达式

10. [各种parse时报错：EOL while scanning string literal](https://blog.csdn.net/idevcod/article/details/11635479)  

    `异常处理 - 用三引号包围错误字符串` 或 `pd.read_json可以避免parse问题`
11. 按值删除，先用.isin把特定值取成NaN，再stack()  

12. excel写入增量或一表多sheet： 构造类 writer = pd.ExcelWriter（name）然后循环写入 df.to_excel(writer, sheet_name='%s' % (i))  

13. 使用.format()[格式化输出](http://www.cnblogs.com/fat39/p/7245035.html)更全面，可以输出set不需要像%写成(1,2,)，可以直接输出百分数，通过位置属性下标等输出。  

14.统计非空值：.nunique() = .count() = .unique().dropna().shape\[0]  
  统计空值：.isnull().sum()  

15. 合并多个df：pd.concat([list of df],axis=1,0)  

16. 连续读写excel:  
    `writer = pd.ExcelWriter(filename) df = pd.to_excel(writer, sheet_name=)`  

17. [df中把数据处理成字符串的方法](http://www.ppvke.com/Blog/archives/39790)  
    `https://www.cnblogs.com/P--K/p/8443995.html`  

# numpy
1. [多项式拟合](https://blog.csdn.net/lubin2016/article/details/78823013)  

2. array扁平化和“逆扁平化"
    `series.flatten() df[:,None]`  

# matplotlib&seaborn
1. [mac下中文标签显示](http://skyrover.me/2018/02/13/matplotlib_issue_solution/)

2. 双坐标轴及xticks修改  
    (https://segmentfault.com/a/1190000006158803)  
    (https://stackoverflow.com/questions/8384120/equivalent-function-for-xticks-for-an-axessubplot-object)
 
    
3. plt.annotate() 数据标注  

4. [seaborn用heatmap画相关性图](http://seaborn.pydata.org/examples/many_pairwise_correlations.html#plotting-a-diagonal-correlation-matrix)  

# scipy & sklearn
1. [统计函数库scipy.stats](https://blog.csdn.net/pipisorry/article/details/49515215)  

2. [一些情况下对数据取log的原因](http://bbs.pinggu.org/thread-3027640-1-1.html)：
    - [拟合正态 - “尖峰肥尾”](http://bbs.pinggu.org/thread-1286098-1-1.html)

3. [PCA降维](https://www.jianshu.com/p/4528aaa6dc48)  (https://blog.csdn.net/baoyan2015/article/details/53742052)

4. [余弦相似度](http://blog.christianperone.com/2013/09/machine-learning-cosine-similarity-for-vector-space-models-part-iii/)  
    `from sklearn.metrics.pairwise import cosine_similarity`  
        `cosine_similarity([[array[0],array[1]]) or cosine_similarity(df)`

5. 将中文数据转换为数值数据：哑变量  
    `pd.get_dummies`
6. [决策树](http://www.ppvke.com/Blog/archives/44548)，将连续变量变成离散：bins  
    [决策树实例](https://blog.csdn.net/oxuzhenyi/article/details/76427704)
    
7. [expected 2D array, got 1D array](https://blog.csdn.net/little_bobo/article/details/78861578):  
    `.values.reshape(-1,1)对于列  
    .values.reshape(1,-1)对于列`  

# mac
1. Crontab命令
    > crontab -e : 启用编辑
     crontab -l : 查看定时任务  
     crontab -r : 删除定时任务 
     sudo touch /etc/crontab ：创建
     sudo /usr/sbin/cron start ：启动 
     sudo /usr/sbin/cron restart ：重启 
     sudo /usr/sbin/cron stop： 停止
     输入crontab -e
     按下a键进入到编辑模式
     输入 0 */1 * * * /home/work/start-service.sh(绝对路径）
     同时按下ctrl+c退出编辑模式
     按下shift+: 输入wq 退出 crontab `
    
# sql
1. 以下方法会导致全表查询：  
    - 在where中使用!=或<> 改为 between  
    - null 改为 = 0  
    - or 改为 union  
    - (not)in  
    
2. 从sql导出的数字类字符串数据，read到pandas的时候,dtype='str'必须写，否则00123变成123  

3. 按天/月/年排序，若原字段只有详细时间，转换为to_char(time, 'YYYY-MM-DD') as d group by d  

# jupyter
1. `%run ====用来运行代码脚本`   
    `%store ====命令可以在两个notebook文件之间传递变量`  
    `%pwd 当前路径`
    `函数末尾加上一个分号,作图不输出`  
    `!cd 来切换目录; !ls用来显示当前目录内容；！pip install或者！conda install用来使用cmd下的命令操作`  
    
2. [jupyter 大礼包](https://www.jianshu.com/p/dacc6acba00b)
