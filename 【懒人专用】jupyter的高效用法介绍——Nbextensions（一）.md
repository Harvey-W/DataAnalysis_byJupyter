
`Dedicated to Cheng.Tan`

## 背景介绍

 用过Chrome或者Firefox的coder肯定都知道插件是一种多么方便的存在——神说：要dock栏，要没广告，要一键翻墙……于是就有Infinity, AdBlock, Tampermonkey…  
那么，作为提倡简洁与高(才)效(没)率(有)的Python，就肯定会有百般懒人如我，去开发一些[神奇插件](https://github.com/ipython-contrib/jupyter_contrib_nbextensions)，比如:  

（我的jupyter）
![%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202018-12-03%20%E4%B8%8B%E5%8D%884.56.09.png](attachment:%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202018-12-03%20%E4%B8%8B%E5%8D%884.56.09.png)  
（原生jupyter界面）
![%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202018-12-03%20%E4%B8%8B%E5%8D%884.55.26.png](attachment:%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202018-12-03%20%E4%B8%8B%E5%8D%884.55.26.png)  
安装过程略简单，这里就不(犯)介(懒)绍(癌)了，来看看这些功能都能给coding带来哪些efficiency~

## Jupyter Nbextensions 功能介绍

![image.png](attachment:image.png)

- 生成目录 [Table of Contents]  

  使用率 ★★★★★

![Dec-03-2018%2019-35-36.gif](attachment:Dec-03-2018%2019-35-36.gif)

> 写长篇数据分析过程必备，可以让分析过程更有条理和侧重。原理类似于锚标记，可以修改目录显示在页面内部还是左侧悬浮窗内，还可以隐藏和显示标题的编号

- 预加载代码块 [Snippets & Snippets Menu & Initialization cells]

  使用率 ★★★★★

![Dec-03-2018%2019-48-31.gif](attachment:Dec-03-2018%2019-48-31.gif)

> 虽然外建.py文件然后利用magic命令也能实现，不过snippets提供更可视化的操作，更多的类型支持，而且最厉害的是还提供各种包的预设模版，不需要自己编辑直接就可以加载十八般武器，配合Initialization cells可以打开文件即自动执行加载包，提取数据，初始化类等各种操作，十分酸爽！

- 草稿本和变量管理 [Scratchpad & Variable Inspector]

  使用率 ★★★★★

![Dec-03-2018%2020-41-35.gif](attachment:Dec-03-2018%2020-41-35.gif)

> 懒人神器！！！我就是不喜欢新建一个cell打草稿，又破坏顺序又容易误删别的内容。scratchpad即开即用，且与主页面内容共享，.head()预览，画个临时图，双开执行别提有多惬意了。同时面对jupyter的cell执行特性，这样做会产生许多垃圾变量或者重复变量，直接打开inspector删删删，缓存就释放干净了

- 快捷键编辑 [Keyboard shortcut editor]

  使用率 ★★★★★

> 让所有extensions变得飞速的终极武器，几乎支持所有的extensions以及jupyter原生的命令的键盘映射。提供一套我的模版：草稿本s，变量管理+，中止执行esc/esc，合并cells cmd+m， 变markdown m，移动/恢复cells，c&v&z， 生成多级标题 1～4， 删除cells d/d ……暂时形成习惯的就这么多

- 冻结或只读cells [Freeze]

  使用率 ★★★★

![Dec-03-2018%2021-12-04.gif](attachment:Dec-03-2018%2021-12-04.gif)

> 将cell的状态变成可以执行不可修改，或者不可执行不可修改的状态。

- 美化代码 [code prettify & 2to3 Converter]

  使用率 ★★★★

![Dec-03-2018%2021-29-27.gif](attachment:Dec-03-2018%2021-29-27.gif)

> 敲一下（锤子图标）就自动补齐空格，长代码换行，完全按照autopep8的规范，专治各种对代码统一的强迫症。飞一下（火箭图标）py2和py3代码互转，什么print加括号，不兼容的包提示安装都自动搞定！再也不用担心看不懂别人的代码了。

（TO BE CONTINUED）

---

`作者：Harvey 原帖来自https://github.com/Harvey-W 写一点数据分析和自己的小玩意儿 欢迎拍砖！`
