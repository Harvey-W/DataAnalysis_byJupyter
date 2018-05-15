# pandas
1. [生成时间序列](https://blog.csdn.net/you_are_my_dream/article/details/70209757)
    
    `pd.date_range(start, end, freq, tz, closed)`
  
2. 由于pandas和python特性，避免io读取和for循环以提高获取数据速度
     - read_sql 改为 read_csv，本地读取百万级以上的数据  
     - pd.read_csv(chunk_size=100)可大幅提高读写速度(300万条数据4分钟),但是读取的数据是generator      
     - [重要][优化代码执行速度](https://python.freelycode.com/contribution/detail/1083)  ：采用apply或向量化

3. [熟练使用交互可视化](http://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html)

    `import ipywidgets as widgets`
    
4. 行列操作

    `df.loc[index]=value`行  
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

# numpy
1. [多项式](https://blog.csdn.net/lubin2016/article/details/78823013)


# matplotlib
1. [mac下中文标签显示](http://skyrover.me/2018/02/13/matplotlib_issue_solution/)

2. [双坐标轴及xticks修改](https://segmentfault.com/a/1190000006158803)

    `ax2 = df.plot(secondary_y = True)`
    
# scipy
1. [统计函数库scipy.stats](https://blog.csdn.net/pipisorry/article/details/49515215)  

2. [一些情况下对数据取log的原因](http://bbs.pinggu.org/thread-3027640-1-1.html)：
    - [拟合正态 - “尖峰肥尾”](http://bbs.pinggu.org/thread-1286098-1-1.html)

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
