## Day01 - 初识Python

### Python简介

> Python（英国发音：/ˈpaɪθən/ 美国发音：/ˈpaɪθɑːn/）, 是一种面向对象的解释型计算机程序设计语言，由荷兰人Guido van Rossum于1989年发明，第一个公开发行版发行于1991年。

Python语法简洁清晰，特色之一是强制用空白符（white space）作为语句缩进。 Python具有丰富和强大的库。它常被昵称为胶水语言，能够把用其他语言制作的各种模块（尤其是C/C++）很轻松地联结在一起。

#### Python简史

![](https://upload-images.jianshu.io/upload_images/13641355-f41d23b70bef9eed.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

具体细节参考博文：[《Python简史》](http://www.cnblogs.com/vamei/archive/2013/02/06/2892628.html)

#### Python的优缺点

**优点**：

+ 简洁明了，对新手友好
+ 解释型语言，天生具有可移植特性
+ 支持两种主流范式变成：面向对象编程和函数式编程
+ 可扩展性和可嵌入性：可调用C/C++代码，也可在C/C++中使用Python代码
+ 代码规范程度高，易读性强

**缺点**：

+ 执行效率低，所以密集型计算的地方可使用C/C++代替
+ 代码无法加密
+ 开发时可选择的框架太多，有选择的地方就有错误

#### Python的应用领域

目前Python在云基础设施、DevOps、网络爬虫开发、数据分析挖掘、机器学习等领域都有着广泛的应用，因此也产生了Web后端开发、数据接口开发、自动化运维、自动化测试、科学计算和可视化、数据分析、量化交易、机器人开发、图像识别和处理等一系列的职位。

### 搭建Python开发环境

#### Windows环境

[官网](https://www.python.org/)自行安装。

#### Linux环境

参考[这里](参考:[https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/Day01/%E5%88%9D%E8%AF%86Python.md)

#### MacOS环境

参考[这里](参考:[https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/Day01/%E5%88%9D%E8%AF%86Python.md)

### 试运行

#### 查看版本信息

```shell
# cmd运行
python --version

# 也可进入python交互模式后再查询
python
import sys
print(sys.version)
print(sys.version_info)
```

#### 第一行Python代码

使用文本编辑器编辑以下代码：

```python
print('hello python!')
```

保存为`.py`格式文件，如hello.py。

使用命令行执行以下代码即可看到结果：

```shell
python hello.py
```

#### 注释

```python
# 单行注释：# 后的内容进行注释
print('# 注释')
# print('# 注释')

# 多行注释：对三个引号开头，三个引号结束的代码块进行注释
'''
print('多行')
print('注释')
'''
```

### 今日练习

1. 执行下面的代码，并翻译执行后的内容

   ```python
   import this
   ```

   执行结果：

   [查看原文和翻译](https://github.com/fongzhizhi/Python-100-Days/blob/master/Day01-15/Day01/res/this.txt)

2. 使用`turtle`绘制图形（了解）

   `Turtle`是Python内置的标准库，可用于绘制各种形状和图案。想象在互

   [官方文档：turtle海龟绘图](https://docs.python.org/zh-cn/3.7/library/turtle.html)

   

   

