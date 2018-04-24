# pandas
1. [生成时间序列](https://blog.csdn.net/you_are_my_dream/article/details/70209757)

    `pd.date_range(start, end, freq, tz, closed,)`
  
2. 由于pandas和python特性，避免io读取和for循环以提高获取数据速度（仍未解决）
    > read_sql 改为 read_csv，本地读取
    > pd.read_csv(chunk_size=100)可大幅提高读写速度(300万条数据4分钟),但是读取的数据没法使用

3. [熟练使用交互可视化](http://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html)

    `import ipywidgets as widgets`
    
4. 行列操作

    `df.loc[index]=value`行  
    `df[columns]=value`列  
    `df.apply(lambda x:x.idxmax(), axis=1)`极值行列  
 
5. bins之后columns需要转换成object类型
