## 语法进阶

### 1、数据结构和算法

**算法**：解决问题的方法和步骤

**算法的优劣**：渐进时间复杂度和渐进空间复杂度

常见算的的渐近时间复杂度的大O标记：

- [![img](https://camo.githubusercontent.com/cef517c8b5e6dd4733128e347aa4b7caaedeb68f/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286329)](https://camo.githubusercontent.com/cef517c8b5e6dd4733128e347aa4b7caaedeb68f/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286329) - 常量时间复杂度 - 布隆过滤器 / 哈希存储
- [![img](https://camo.githubusercontent.com/1531d9af073a70fd2a3dbe64a84bf07b38ff23ac/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286c6f675f326e29)](https://camo.githubusercontent.com/1531d9af073a70fd2a3dbe64a84bf07b38ff23ac/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286c6f675f326e29) - 对数时间复杂度 - 折半查找（二分查找）
- [![img](https://camo.githubusercontent.com/d6667cc782db1c37003a190b5ad1c6770fd7ca7b/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e29)](https://camo.githubusercontent.com/d6667cc782db1c37003a190b5ad1c6770fd7ca7b/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e29) - 线性时间复杂度 - 顺序查找 / 桶排序
- [![img](https://camo.githubusercontent.com/20bf7830a5fad1deddaa264fde9ca5557b8e1425/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e2a6c6f675f326e29)](https://camo.githubusercontent.com/20bf7830a5fad1deddaa264fde9ca5557b8e1425/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e2a6c6f675f326e29) - 对数线性时间复杂度 - 高级排序算法（归并排序、快速排序）
- [![img](https://camo.githubusercontent.com/1db7c9094a5635d43a5826e4a1e989dbd0028ccc/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e5e3229)](https://camo.githubusercontent.com/1db7c9094a5635d43a5826e4a1e989dbd0028ccc/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e5e3229) - 平方时间复杂度 - 简单排序算法（选择排序、插入排序、冒泡排序）
- [![img](https://camo.githubusercontent.com/e5a92b18b84f296fa24d8646d3732673dadbcb26/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e5e3329)](https://camo.githubusercontent.com/e5a92b18b84f296fa24d8646d3732673dadbcb26/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e5e3329) - 立方时间复杂度 - Floyd算法 / 矩阵乘法运算
- [![img](https://camo.githubusercontent.com/c8cf1b1c2ed8f9da4154a2da52828896f105d3a0/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f28325e6e29)](https://camo.githubusercontent.com/c8cf1b1c2ed8f9da4154a2da52828896f105d3a0/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f28325e6e29) - 几何级数时间复杂度 - 汉诺塔
- [![img](https://camo.githubusercontent.com/2952a64273b413458526e5d34076903226223e25/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e2129)](https://camo.githubusercontent.com/2952a64273b413458526e5d34076903226223e25/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e2129) - 阶乘时间复杂度 - 旅行经销商问题 - NP

![](https://upload-images.jianshu.io/upload_images/13641355-cf4b530674136fc3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![](https://upload-images.jianshu.io/upload_images/13641355-ae4dd5d185f604de.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 排序算法

##### 选择排序

最简单直观的排序方法，从一组**待排序**的序列中选择最大值或最小值放在序列的最前面，循环，直到所有待排序元素排完。

```python
def select_sort(items, comp = lambda x, y: x < y):
	for i in range(len(items)-1):
		min_index = i
		for j in range(i+1, len(items)):
			if comp(items[j], items[min_index]):
				min_index = j
		items[i], items[min_index] = items[min_index], items[i]
	return items
```

注：这里的comp参数是一个匿名函数。关键字`lambda`是匿名函数的表达式标志，Python里的匿名函数需要用一句表达式得到返回结果。比如求和的匿名函数可以写成：

```python
add = lambda x, y : x + y
```

##### 冒泡排序

冒泡排序就是在遍历待排序列的过程中进行**两两相邻比较**，比如默认从小到大排序，那么每一趟排序，最大的那个值就会慢慢移动到最末端，就像水中的气体冒泡一样。

```python
def bubbleSort(items, comp=lambda x, y: x < y):
	for i in range(len(items) - 1):
		for j in range(len(items) - i - 1):
			if comp(items[j+1], items[j]):
				items[j], items[j+1] = items[j+1], items[j]
	return items
```

下面是冒泡排序的升级版：

```python
def bubble_sort(origin_items, comp=lambda x, y: x > y):
	"""高质量冒泡排序"""
	items = origin_items[:]
	for i in range(len(items) - 1):
		swapped = False
		for j in range(i, len(items) - 1 - i):
			if comp(items[j], items[j + 1]):
				items[j], items[j + 1] = items[j + 1], items[j]
				swapped = True
		if swapped:
			swapped = False
			for j in range(len(items) - 2 - i, i, -1):
				if comp(items[j - 1], items[j]):
					items[j], items[j - 1] = items[j - 1], items[j]
					swapped = True
		if not swapped:
			break
	return items
```

##### 归并排序

归并排序是在归并操作的基础上进行的排序，是`分治法`的典型应用，适合大规模数据排序，但比较消耗内存，将待排序列分解到两两一组，然后排序，排序之后依次合并，直到合并为完整序列。观察下图可以很直观地理解归并排序的逻辑：

![](https://upload-images.jianshu.io/upload_images/13641355-a39e26b594fa254a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
def mergeSort(items, comp=lambda x, y:x < y):
	length = len(items)
	if length <= 1: #当一个元素时即为有序
		return items
	mid = length // 2
	left = mergeSort(items[:mid], comp)
	right = mergeSort(items[mid:], comp)
	return merge(left, right, comp)

#归并操作:两个有序数列合并为一个
def merge(list1, list2, comp=lambda x, y:x < y):
	len1 = len(list1)
	len2 = len(list2)
	newList = []
	i, j=  0, 0
	while i < len1 or j < len2:
		if j == len2 or (i != len1 and comp(list1[i], list2[j])):
			newList.append(list1[i])
			i += 1
		else:
			newList.append(list2[j])
			j += 1
	return newList
```

##### 快速排序

快速排序也是`分治`思想的一种运用，先随机选择一个“基点”，从基点的左和右开始遍历序列，小于基点数的放在左边，大于基点数的放在右边。依次对左右序列进行快排，最终返回的**左序列+基点数+右序列**就是快排后的完整序列。

```python 
def quickSort(items, comp=lambda x, y:x < y):
	length = len(items)
	if length <= 1:
		return items
	pos, l, r = 0, 1, len(items) - 1 #基准,左右
	while l <= r:
		if comp(items[l], items[pos]):
			items.insert(0, items.pop(l))
			pos += 1
		if comp(items[r], items[pos]):
			items.insert(0, items.pop(r))
			pos += 1
		l += 1
		r -= 1
	left = quickSort(items[:pos], comp)
	right = quickSort(items[pos+1:], comp)
	return left + [items[pos]] +right
```

#### 查找算法

##### 顺序查找

顾名思义，直接遍历查找：

```python
def seq_search(items, key):
	for i, item in items:
		if item == key:
			return i
	return -1
```

##### 折半查找

折半查找要求查找的序列是有序的：

```python
def bin_search(items, key):
	start, end = 0, len(items) - 1
	while start <= end:
		mid = (start + end) // 2
		if key > items[mid]:
			start = mid + 1
		elif key < items[mid]:
			end = mid - 1
		else:
			return mid
	return -1
```

### 2、一些语法和工具

#### 推导式的使用

推导式像匿名函数一样简化了书写格式。

##### 列表推导式

> 语法：[expr for value in collection ifcondition]

```python
#返回大于100的新序列
list1 = [191.88, 1186.96, 149.24, 48.44, 166.89, 208.09, 21.29]
list2 = [val for val in list1 if val > 100]
print(list2)
```

##### 字典推导式

> 语法：{ key_expr: value_expr for key, value in collection if condition }

```python
# 用股票价格大于100元的股票构造一个新的字典
prices = {
	'AAPL': 191.88,
	'GOOG': 1186.96,
	'IBM': 149.24,
	'ORCL': 48.44,
	'ACN': 166.89,
	'FB': 208.09,
	'SYMC': 21.29
}
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)
```

##### 集合推导式

> 语法：{ expr for value in collection if condition }

```python
#返回长度大于2的新集合
oldset = {'hello', 'e', 'i', 'ok', 'okk', 'world', 'jinx'}
newset = {item for item in oldset if len(item) > 2}
print(newset)
```

#### heapq、itertools模块等的用法

##### headpq

```python
"""
从列表中找出最大的或最小的N个元素
堆结构(大根堆/小根堆)
"""
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
	{'name': 'IBM', 'shares': 100, 'price': 91.1},
	{'name': 'AAPL', 'shares': 50, 'price': 543.22},
	{'name': 'FB', 'shares': 200, 'price': 21.09},
	{'name': 'HPQ', 'shares': 35, 'price': 31.75},
	{'name': 'YHOO', 'shares': 45, 'price': 16.35},
	{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3, list1)) #最大
print(heapq.nsmallest(3, list1)) #最小
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))
```

更多用法请参考这里:[堆队列算法](https://docs.python.org/zh-cn/3.7/library/heapq.html?highlight=heapq)

##### itertools

```python
"""
迭代工具 - 排列 / 组合 / 笛卡尔积
"""
import itertools

def show(iter):
	for item in iter:
		print(item)

a = itertools.permutations('ABCD', 2) #排列
b = itertools.combinations('ABCDE', 3) #组合
c = itertools.product('ABCD', '123') #笛卡尔积

print('---排列---')
show(a)
print('---组合---')
show(b)
print('---笛卡尔积---')
show(c)
```

更多用法请参考这里:[为高效循环而创建迭代器的函数](https://docs.python.org/zh-cn/3.7/library/itertools.html?highlight=itertools)

#### collections模块下的工具类

```python
"""
找出序列中出现次数最多的元素
"""
from collections import Counter

words = [
	'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
	'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
	'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
	'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))
```

更多用法请参考这里:[容器数据类型](https://docs.python.org/zh-cn/3.7/library/collections.html?highlight=collection#module-collections)

### 3、常用算法

#### 穷举法

穷举法就是把所有可能出现的情况都验证一遍。以下是“百钱百鸡”的穷举法：

```python
# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只

i, j, k = 5, 3, 1/3
rangex = 100 // i + 1
rangey = 100 // j + 1
for x in range(0, rangex):
	for y in range(0, rangey):
		z = 100 - x - y
		if (x*i + y*j + z*k) == 100:
			print('x:%d,y:%d,z:%d' % (x, y, z))
```

#### 贪婪算法

**贪心算法**（英语：greedy algorithm），又称**贪婪算法**，是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是最好或最优的[算法](https://zh.wikipedia.org/wiki/%E7%AE%97%E6%B3%95)。

假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品（各一件）。很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品。

| 名称   | 价格（美元） | 重量（kg） |
| ------ | ------------ | ---------- |
| 电脑   | 200          | 20         |
| 收音机 | 20           | 4          |
| 钟     | 175          | 10         |
| 花瓶   | 50           | 2          |
| 书     | 10           | 1          |
| 油画   | 90           | 9          |

我们发现，小偷肯定是希望每公斤能装更值钱的东西，按照这个思路，可以这样理解，**小偷每次拿的都是单公斤最值钱的东西**，即不考虑没有装满这种情况。这也是贪婪算法的思维，保证每一步最优：

```python
"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
油画 90 9
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
"""
things = {
	'油画': [90, 9],
	'电脑': [200, 20],
	'收音机': [20, 4],
	'钟': [175, 10],
	'花瓶': [50, 2],
	'书': [10, 1]
}

#为了方便分析，我们构造一个类
class Thing(object):
	"""物品"""
	def __init__(self, name, price, weight):
		self.name = name
		self.price = price
		self.weight = weight

	@property
	def value(self):
		"""价格重量比"""
		return self.price / self.weight

def main():
	"""主函数"""
	max_weight = 20 #总重量
	all_things = []
	for name in things:
		all_things.append(Thing(name, things[name][0], things[name][1]))

	all_things.sort(key=lambda x: x.value, reverse=True) #按照物品价值排序，依次取即可
	total_weight = 0
	total_price = 0
	for thing in all_things:
		if total_weight + thing.weight <= max_weight:
			print(f'小偷拿走了{thing.name}')
			total_weight += thing.weight
			total_price += thing.price
	print(f'总价值: {total_price}美元')

if __name__ == '__main__':
	main()
```

#### 分治法

在[计算机科学](https://zh.wikipedia.org/wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6)中，**分治法**是建基于多项分支[递归](https://zh.wikipedia.org/wiki/%E9%80%92%E5%BD%92)的一种很重要的算法[范式](https://zh.wikipedia.org/wiki/%E7%AF%84%E5%BC%8F)。字面上的解释是“分而治之”，就是把一个复杂的问题分成两个或更多的相同或相似的子问题，直到最后子问题可以简单的直接求解，原问题的解即子问题的解的合并。（维基百科）

简单来说就是“大事化小，小事化了”的逻辑。

典型应用如归并排序、快速排序

#### 回溯法

**回溯法**（英语：backtracking）是[暴力搜索法](https://zh.wikipedia.org/wiki/%E6%9A%B4%E5%8A%9B%E6%90%9C%E5%B0%8B%E6%B3%95)中的一种。

对于某些计算问题而言，回溯法是一种可以找出所有（或一部分）解的一般性算法，**尤其适用于约束满足问题**（在解决约束满足问题时，我们逐步构造更多的候选解，并且在确定某一部分候选解不可能补全成正确解之后放弃继续搜索这个部分候选解本身及其可以拓展出的子候选解，转而测试其他的部分候选解）。

在经典的教科书中，**八皇后问题**展示了回溯法的用例。（八皇后问题是在标准国际象棋棋盘中寻找八个皇后的所有分布，使得没有一个皇后能攻击到另外一个。）

回溯法采用[试错](https://zh.wikipedia.org/wiki/%E8%AF%95%E9%94%99)的思想，它尝试分步的去解决一个问题。在分步解决问题的过程中，当它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问题的答案。回溯法通常用最简单的[递归](https://zh.wikipedia.org/wiki/%E9%80%92%E5%BD%92)方法来实现，在反复重复上述的步骤后可能出现两种情况：

- 找到一个可能存在的正确的答案
- 在尝试了所有可能的分步方法后宣告该问题没有答案

在最坏的情况下，回溯法会导致一次[复杂度](https://zh.wikipedia.org/wiki/%E8%AE%A1%E7%AE%97%E5%A4%8D%E6%9D%82%E6%80%A7%E7%90%86%E8%AE%BA)为[指数时间](https://zh.wikipedia.org/wiki/%E6%8C%87%E6%95%B8%E6%99%82%E9%96%93)的计算。

（以上来自维基百科）

【案例：骑士巡逻】

**骑士巡逻**（英语：Knight's tour）是指在按照[国际象棋](https://zh.wikipedia.org/wiki/%E5%9B%BD%E9%99%85%E8%B1%A1%E6%A3%8B)中[骑士](https://zh.wikipedia.org/wiki/%E9%A9%AC_(%E5%9B%BD%E9%99%85%E8%B1%A1%E6%A3%8B))的规定走法走遍整个[棋盘](https://zh.wikipedia.org/wiki/%E6%A3%8B%E7%9B%A4)的每一个方格，而且每个网格只能够经过一次。

假若骑士能够从走回到最初位置，则称此巡逻为“封闭巡逻”，否则，称为“开巡逻”。对于8*8棋盘，一共有26,534,728,821,064种封闭巡逻，但是到底有多少种开巡逻仍然未知。

（以上来自维基百科）

#### 动态规划

**动态规划**（英语：Dynamic programming，简称DP）是一种在[数学](https://zh.wikipedia.org/wiki/%E6%95%B0%E5%AD%A6)、[管理科学](https://zh.wikipedia.org/wiki/%E7%AE%A1%E7%90%86%E7%A7%91%E5%AD%A6)、[计算机科学](https://zh.wikipedia.org/wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6)、[经济学](https://zh.wikipedia.org/wiki/%E7%BB%8F%E6%B5%8E%E5%AD%A6)和[生物信息学](https://zh.wikipedia.org/wiki/%E7%94%9F%E7%89%A9%E4%BF%A1%E6%81%AF%E5%AD%A6)中使用的，通过把原问题分解为相对简单的子问题的方式求解复杂问题的方法。

动态规划常常适用于有重叠子问题[[1]](https://zh.wikipedia.org/wiki/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92#cite_note-1)和[最优子结构](https://zh.wikipedia.org/w/index.php?title=%E6%9C%80%E4%BC%98%E5%AD%90%E7%BB%93%E6%9E%84&action=edit&redlink=1)性质的问题，动态规划方法所耗时间往往远少于朴素解法。

动态规划背后的基本思想非常简单。大致上，若要解一个给定问题，我们需要解其不同部分（即子问题），再根据子问题的解以得出原问题的解。

通常许多子问题非常相似，为此动态规划法试图仅仅解决每个子问题一次，从而减少计算量：一旦某个给定子问题的解已经算出，则将其[记忆化](https://zh.wikipedia.org/wiki/%E8%AE%B0%E5%BF%86%E5%8C%96)存储，以便下次需要同一个子问题解之时直接查表。这种做法在重复子问题的数目关于输入的规模呈[指数增长](https://zh.wikipedia.org/wiki/%E6%8C%87%E6%95%B8%E5%A2%9E%E9%95%B7)时特别有用。

（以上来自维基百科）

### 4、函数的使用方式

#### 将函数视为“一等公民”

+ 函数可以赋值给变量
+ 函数和作为函数的参数
+ 函数可作为函数的返回值

#### 高级函数之map & filter以及替代品

##### map

`map`函数用来遍历给定序列并返回遍历后的计算值所组成的迭代器（2.x是直接返回列表）

语法：

> map(function, iterable, ...)

参数：

function：第一个参数为操作序列元素的函数，序列元素作为函数参数进行计算

iterable：有限个可迭代对象，作为函数处理的参数

返回值：2.x版本返回新的列表，3.x返回迭代器

示例如下：

```python
def main():
    
	def square(x):
		return x ** 2
	
	list1 = map(square, [1, 2, 3, 4, 5]) #返回参数列表平方
	print(list(list1)) #[1, 4, 9 ,16 ,25]

	list2 = map(lambda x,y:x + y, [1, 2, 3, 4, 5], [6, 7, 8]) #使用匿名函数, 返回列表和
	print(list(list2)) #[7, 9, 11]

if __name__ == '__main__':
	main()
```

##### filter

`filter`函数用于过滤给定序列中符合条件的元素，返回新的序列。

语法：

> filter(function, iterable)

参数：

function：过滤元素的函数，判断元素是否符合过滤条件

iterable：迭代对象

实例：

```python
def main():

	def filterFunc(x):
		return x % 3 == 0
	
	list1 = filter(filterFunc, [1, 3, 5, 7, 9])
	print(list(list1)) #[3, 9]

if __name__ == '__main__':
	main()
```

##### 结合使用以及替代写法

```python
def main():
    
	list1 = map(lambda x: x ** 2, filter(lambda x:x % 2 == 0, range(0, 10)))
	list2 = [x ** 2 for x in range(0, 10) if x % 2 == 0]
	print(list(list1)) #替代写法
	print(list2)
	

if __name__ == '__main__':
	main()
```

#### 位置参数、可变参数、关键字参数、命名关键字参数

##### 位置参数

位置参数就是最基本的参数形式，按照函数定义时的参数位置进行传入。

```python
#name和age的位置固定，使用这个函数fun也需要根据定义的位置传入
def fun(name, age)
	pass
```

##### 默认参数

当参数有默认值时我们就不需要特殊处理和传入，我们可以使用默认参数来实现：

```python
#默认age参数为18
def fun(name, age=18):
    print('name=%s, age=%d' % (name, age))

#使用：
fun('jinx', 20)
fun('yasuo')
```

需要注意的是，位置参数必须写在默认参数之前，下面这种写法就会报错：

```python
#错误的参数定义
def fun(age=18, name)
	pass
```

##### 关键字参数

用于函数调用而非定义，使用”键=值“的形式进行参数调用。使用关键字参数的优点是：参数的含义更清晰；无需考虑位置参数的限制。

需要注意的是：关键字参数和位置参数同样能混合使用，但是位置参数必须写在关键字参数之前。写在后面的关键字参数无需考虑顺序。

```python
def fun(name, age):
	print('name=%s, age=%d' % (name, age))
    
#使用关键字参数
fun(name='jinx', age=20)
fun(age=19, name='yauso')
fun('anny', age=10)

#错误的示范
fun(10, name='anny')
fun(age=10, 'anny')
fun(name='anny', 10)
```

##### 可变参数

当我们不确定需要传入几个参数时就可以使用可变参数，可变参数有两种写法：

+ 可变位置参数

  ```python
  #求和
  def sum(*nums):
      n = 0
      for x in nums:
      	n += x
      print(n)
  #使用
  sum(1, 2, 3)
  sum(1, 2, 3, 4, 5 ,6)
  ```

+ 可变关键字参数

  ```python
  #打印个人信息
  def printInfo(**person):
      for k in person:
      	print(k+':'+person[k], '\r')
  #使用
  printInfo(name='jinx', age='19', sex='girl')
  printInfo(name='yasuo', position='middle', belief='happiness')
  ```

##### 各种类型的参数混合使用

```python
#个人信息统计
#name
def fun(name, age=18, *dream_datas, **families):
    pass
```

#### 参数的元信息（增加代码可读性）

使用函数参数注解是一个很好的办法，它能提示程序员怎样正确使用这个函数。

```python
def fun(x:int) -> str:
	print(x)

fun(1)
fun('a')
```

python解释器不会对这些注解添加任何的语义。它们不会被类型检查，运行时跟没有加注解之前的效果也没有任何差距。 然而，能够增强代码的可读性。第三方工具和框架可能会对这些注解添加语义。同时它们也会出现在文档中。

#### 内联函数之匿名函数

##### 匿名函数lambda

对于那种可以一句表达式就能定义的函数，我们就可以使用匿名函数来表示，比如两数求和：

```python
sum = lambda x, y: x + y
print(sum(1, 2))
```

匿名函数的表达式就是函数的返回值。

lambda只是Python内联函数的一个，还有其他为了提高效率的内联小函数，如：zip,filter, map, reduce等。

#### 闭包和作用域的问题

+ Python搜索变量的LEGB顺序（Local --> Embedded --> Global --> Built-in）

+ `global`和`nonlocal`关键字的作用

  `global`：声明或定义全局变量（要么直接使用现有的全局作用域的变量，要么定义一个变量放到全局作用域）。

  `nonlocal`：声明使用嵌套作用域的变量（嵌套作用域必须存在该变量，否则报错）。

#### 装饰器函数：使用装饰器和取消装饰器

##### 什么是函数装饰器

函数装饰器是可以修改其它函数功能的函数，好比一个功能buff，可以给你想要的函数进行装饰以实现某写功能，且保证了代码的复用率，让整体代码更简洁。

##### 函数装饰器的原理

下面是一个简单的函数：

```python
def sayHi(name='man'):
    print('Hi!', name)
```

加入我们需要在这个函数运行被调用时输出`log日志`，我们可以这样：

```python
def sayHi(name='man'):
    print('sayHi is called.') #打印日志信息
    print('Hi!', name)
```

同样的，如果我们需要对其他函数输出类似的日志，我们就需要写类似的重复代码。所以我们可以**将相同功能的代码封装为一个函数**：

```python
def sayHi(name='man'):
    log(sayHi)
    print('Hi!', name)

def sayHello(name='man'):
    log(sayHello)
    print('Hello!', name)

def log(func):
    print(func.__name__, 'is called.')
```

封装功能函数能提高代码复用率，但我们发现案例中的调用不够优雅，且函数需要作为参数传入，及其麻烦，进一步优化，对日志函数进行改造：

```python
def sayHi(name='man'):
    print('Hi!', name)

def sayHello(name='man'):
    print('Hello!', name)

#日志装饰函数
def log_decorator_fun(func):
    def log():
        print(func.__name__, 'is called.')
        func()
    return log

#使用装饰器函数对函数进行装饰
sayHi = log_decorator_fun(sayHi)
sayHello = log_decorator_fun(sayHello)

sayHi()
```

到这里，装饰器的基本原理已经很明显了，装饰器其实就是利用函数的特性，对原函数进行改造之后再返回具有特定功能的函数。

##### 优雅的使用装饰器

我们发现，通过调用函数的方式来装饰函数不够优雅，在`python`中使用`@ func`的形式修饰一个函数，以达到修饰器的效果。我们对上面的案例进行改写能达到一样的效果：

```python
#日志装饰函数
def log_decorator_fun(func):
    def log():
        print(func.__name__, 'is called.')
        func()
    return log

@log_decorator_fun
def sayHi(name='man'):
    print('Hi!', name)

@log_decorator_fun
def sayHello(name='man'):
    print('Hello!', name)

sayHi()
sayHello()
```

##### 装饰器的问题

在上面的例子中，如果执行下面的语句：

```python
print(sayHi.__name__) # log
```

发现打印的结果为`log`而非函数名本身，这是因为装饰器将函数整个重写了，原来函数本身的属性也会就变了。

我们一般`functools.wraps`函数对我们的装饰器进行再装饰：

```python
from functools import wraps
#日志装饰函数
def log_decorator_fun(func):
    @wraps(func)
    def log():
        print(func.__name__, 'is called.')
        func()
    return log
```

> **注**：`@wraps(func)`接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。

#### 面向对象的相关知识

##### 三大支柱：封装、继承和多态

```python
"""
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""
from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    '''员工(抽象类)'''
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def getSalary(self):
        '''计算工资(抽象方法)'''
        pass

class Manager(Employee):
    '''经理'''
    def getSalary(self):
        return 15000

class Programmer(Employee):
    '''程序员'''
    def __init__(self, name, work_hour=0):
        self.work_hour = work_hour
        super().__init__(name)

    def getSalary(self):
        return 200 * self.work_hour

class Salesman(Employee):
    '''销售员'''
    def __init__(self, name, sales=0):
        self.sales = sales
        super().__init__(name)

    def getSalary(self):
        return 1800 + self.sales * 0.05

class EmployeeFactory():
    '''创建员工的工厂类'''
    @staticmethod
    def create(type, *args, **kwargs):
        emp = None
        if type == 'M':
            emp = Manager(*args, **kwargs)
        elif type == 'P':
            emp = Programmer(*args, **kwargs)
        elif type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp

def main():
    emps = [
        EmployeeFactory.create('M', '曹操'), 
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85), 
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print('%s: %.2f元' % (emp.name, emp.getSalary()))

if __name__ == '__main__':
    main()
```

> 使用`ABCMeta`来创建元类，也就是可继承的抽象类。
>
> 使用`abstractmethod`来抽象函数。

##### 枚举类

> 在[数学](https://baike.baidu.com/item/%E6%95%B0%E5%AD%A6/107037)和[计算机科学](https://baike.baidu.com/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6/9132)理论中，一个集的**枚举**是列出某些有穷序列集的所有成员的程序，或者是一种特定类型对象的计数。
>
> 这两种类型经常（但不总是）重叠。 [1]  是一个被命名的整型常数的集合，枚举在日常生活中很常见，例如表示星期的SUNDAY、MONDAY、TUESDAY、WEDNESDAY、THURSDAY、FRIDAY、SATURDAY就是一个枚举。 --百度百科

**枚举**其实**就是一一列举**的意思。比如我们使用下面这个类来定义交通灯：

```python
class traffic_light():
    '''使用特定的变量表示枚举对象的值'''
    Red, Yellow, Blue = range(3)

print(traffic_light.Red) #0
print(traffic_light.Yellow) #1
print(traffic_light.Blue) #2
```

这样，我们也可以使用这个普通类来一一列举出交通灯所表示的三种颜色。

**但**，这样的类**很不安全**，既然是特定对象的计数，也就相当于常量，那么枚举对象的值就不应该被随意的变更，但是上面这个类在执行了类似`traffic_light.Red = 1`这样的代码后轻易变更了设定的值。这是极不安全的。

一般枚举不应该存在key相同的枚举项（类变量），也不允许在类外直接修改枚举项的值。

所以在`Python`中我们可以使用`enum模块`中的`Enum`对象或者继承之来创建一个枚举类。

```python
from enum import Enum, unique

@unique
class traffic_light(Enum):
    Red, Yellow, Blue = range(3)

#直接访问
print(traffic_light.Red.value) #0
print(traffic_light.Yellow) #traffic_light.Yellow

#迭代展开
for light in traffic_light:
    print(light.name, ':', light.value)
```

Tips：

> + 枚举类不能用来实例化对象
> + 访问枚举类中的某一项，直接使用类名访问加上要访问的项即可，比如 color.YELLOW
> + 枚举类里面定义的Key = Value，在类外部不能修改Value值，也就是说下面这个做法是错误的
>
> + 枚举项可以用来比较，使用==，或者is
>
> + 导入Enum之后，一个枚举类中的Key和Value，Key不能相同，Value可以相，但是Value相同的各项Key都会当做别名。
> + 使用`unique`装饰器可以保证枚举项唯一。
> + 符号常量总是优于字面常量，枚举类型是定义符号常量的最佳选择。

##### 类与类之间的关系

+ is-a：继承
+ has-a：关联
+ use-a：依赖

案例：扑克发牌

```python
from enum import Enum, unique
import random

@unique
class Suite(Enum):
    '''花色'''
    SPADE, HEART, CLUB, DIAMOND = range(4) #黑, 红, 梅, 方

    def __lt__(self, other):
        '''用于排序'''
        return self.value < other.value

class Card():
    '''牌'''
    def __init__(self, suite, face, king):
        self.suite = suite
        self.face = face
        self.king = king

    def show(self):
        '''显示牌'''
        suites = ['♠️', '♥️', '♣️', '♦️']
        faces = ['', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        kings = ['', '☀', '☪'] #另外用两个符号表示大小王
        if self.isKing:
            return kings[self.king]
        else:
            return f'{suites[self.suite.value]}{faces[self.face]}' #python6.3引入的字符串格式化方法f-string

    def __str__(self):
        return self.show()

    def __repr__(self):
        '''打印时显示的描述'''
        return self.show()

    @property
    def isKing(self):
        return self.king

class Poker():
    '''扑克'''
    def __init__(self):
        self.index = 0
        self.cards = [Card(suite, face, False) for suite in Suite for face in range(1, 14)]
        kings = [Card(False, False, k) for k in range(1, 3)]
        self.cards.extend(kings)
    
    def shuffle(self):
        '''洗牌（随机乱序）'''
        random.shuffle(self.cards) #shuffle()方法将序列的所有元素随机排
        self.index = 0

    def deal(self):
        '''发牌'''
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        return self.index < len(self.cards)

class Player():
    '''玩家'''
    def __init__(self, name):
        self.name = name
        self.cards = []
    
    def get_one(self, poker):
        '''抓牌'''
        self.cards.append(poker.deal())

    def sort(self, comp = lambda card: (card.suite, card.face)):
        '''整理手中的牌'''
        sort_card = self.get_sort_card()
        sort_card[0].sort(key = comp)
        self.cards = sort_card[0] + sort_card[1]

    def get_sort_card(self):
        '''获得可排序牌：大小王没有花色不能进行排序'''
        sort_card = filter(lambda card: not card.king, self.cards)
        unsort_card = filter(lambda card: card.king, self.cards)
        return [list(sort_card), list(unsort_card)]

def main():
    poker = Poker()
    poker.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    while poker.has_more:
        for player in players:
            if poker.has_more:
               player.get_one(poker)
    for player in players:
        player.sort()
        print(player.name, end=': ')
        print(player.cards)

if __name__ == '__main__':
    main()
```

> 对于大小王这种不符合规律的牌需要单独处理

##### 对象的复制（深复制/深拷贝/深度克隆和浅复制/浅拷贝/影子克隆）

对象分可分为可变对象（如列表字典）和不可变对象（如整型、浮点型、字符、元组），可变对象可以修改原始值，这就是造成浅克隆的原因。

```python
#不可变对象
'''不可变对象在修改引用对象时无法直接修改原始数据，所以开辟了新空间，也就切断了引用，也就实现了深克隆'''
a = 1
b = a
b = 2
print('a=', a) #a= 1
print('b=', b) #b= 2

#可变对象
'''不可变对象可以直接修改引用的原始数据，并未切断引用，所以是浅克隆'''
a = [1, 2, 3]
b = a
b.append(4)
print('a=', a) #a= [1, 2, 3, 4]
print('b=', b) #b= [1, 2, 3, 4]
```

>  可以发现，要实现深度克隆，本质就是开辟新空间，实现新的引用。

`Python`已经实现了对象的普通克隆和深度克隆。

#普通克隆

```python
a = [1, 2, [3, 4], 5]
b = a.copy() #普通克隆
b.append(6)
print('a=', a) #a= [1, 2, [3, 4], 5]
print('b=', b) #b= [1, 2, [3, 4], 5, 6]

b[2].append(5)
print('a=', a) #a= [1, 2, [3, 4, 5], 5]
print('b=', b) #b= [1, 2, [3, 4, 5], 5, 6]
```

> 普通克隆只是实现了一级深度克隆，更深层次的可变对象还是之前的引用，所以仍然是浅克隆。

#深度克隆

```
from copy import deepcopy

a = [1, 2, [3, 4], 5]
b = deepcopy(a)
b.append(6)
print('a=', a) #a= [1, 2, [3, 4], 5]
print('b=', b) #b= [1, 2, [3, 4], 5, 6]

b[2].append(5)
print('a=', a) #a= [1, 2, [3, 4], 5]
print('b=', b) #b= [1, 2, [3, 4, 5], 5, 6]
```

> 使用`copy`模块的`deepcopy`即可实现深度克隆。
>
> 浅克隆是对象自带的方法，而深度克隆需要导入使用。

##### 垃圾回收、循环引用和弱引用

Python使用了自动化内存管理，这种管理机制以**引用计数**为基础，同时也引入了**标记-清除**和**分代收集**两种机制为辅的策略。

```python
typedef struct_object {
    /* 引用计数 */
    int ob_refcnt;
    /* 对象指针 */
    struct_typeobject *ob_type;
} PyObject;
```

```python
/* 增加引用计数的宏定义 */
#define Py_INCREF(op)   ((op)->ob_refcnt++)
/* 减少引用计数的宏定义 */
#define Py_DECREF(op) \ //减少计数
    if (--(op)->ob_refcnt != 0) \
        ; \
    else \
        __Py_Dealloc((PyObject *)(op))
```

导致引用计数+1的情况：

- 对象被创建，例如`a = 23`
- 对象被引用，例如`b = a`
- 对象被作为参数，传入到一个函数中，例如`f(a)`
- 对象作为一个元素，存储在容器中，例如`list1 = [a, a]`

导致引用计数-1的情况：

- 对象的别名被显式销毁，例如`del a`
- 对象的别名被赋予新的对象，例如`a = 24`
- 一个对象离开它的作用域，例如f函数执行完毕时，f函数中的局部变量（全局变量不会）
- 对象所在的容器被销毁，或从容器中删除对象

引用计数可能会导致循环引用问题，而循环引用会导致内存泄露，如下面的代码所示。为了解决这个问题，Python中引入了“标记-清除”和“分代收集”。在创建一个对象的时候，对象被放在第一代中，如果在第一代的垃圾检查中对象存活了下来，该对象就会被放到第二代中，同理在第二代的垃圾检查中对象存活下来，该对象就会被放到第三代中。

```
# 循环引用会导致内存泄露 - Python除了引用技术还引入了标记清理和分代回收
# 在Python 3.6以前如果重写__del__魔术方法会导致循环引用处理失效
# 如果不想造成循环引用可以使用弱引用
list1 = []
list2 = [] 
list1.append(list2)
list2.append(list1)
```

以下情况会导致垃圾回收：

- 调用`gc.collect()`
- gc模块的计数器达到阀值
- 程序退出

如果循环引用中两个对象都定义了`__del__`方法，gc模块不会销毁这些不可达对象，因为gc模块不知道应该先调用哪个对象的`__del__`方法，这个问题在Python 3.6中得到了解决。

也可以通过`weakref`模块构造弱引用的方式来解决循环引用的问题。

##### 魔法属性和方法（请参考《Python魔法方法指南》）

> 什么是魔法方法呢？它们在面向对象的Python中处处皆是。它们是一些可以让你对类添加“魔法”的特殊方法。 它们经常是两个下划线包围来命名的（比如 `__init__`，` __lt__` ）。但是现在没有很好的文档来解释它们。 所有的魔法方法都会在Python的官方文档中找到，但是它们组织松散。而且很少会有示例（有的是无聊的语法描述， 语言参考）。
>
> 所以，为了修复我感知的Python文档的缺陷，我开始提供更为通俗的，有示例支持的Python魔法方法指南。我一开始 写了一些博文，现在我把这些博文总起来成为一篇指南。

可参考：[Python魔法方法指南_博客](https://pycoders-weekly-chinese.readthedocs.io/en/latest/issue6/a-guide-to-pythons-magic-methods.html)

##### Mixin模式

类似`java`使用接口来实现多继承的方式。`Python`中没有接口，这种Mixin混合类就类似接口，形式上使用起来像多继承，实则还是遵循了单继承原则。

可参考:[关于Python的Mixin模式](https://www.cnblogs.com/aademeng/articles/7262520.html)

##### 元编程和元类

##### 面向对象设计原则

- 单一职责原则 （**S**RP）- 一个类只做该做的事情（类的设计要高内聚）
- 开闭原则 （**O**CP）- 软件实体应该对扩展开发对修改关闭
- 依赖倒转原则（DIP）- 面向抽象编程（在弱类型语言中已经被弱化）
- 里氏替换原则（**L**SP） - 任何时候可以用子类对象替换掉父类对象
- 接口隔离原则（**I**SP）- 接口要小而专不要大而全（Python中没有接口的概念）
- 合成聚合复用原则（CARP） - 优先使用强关联关系而不是继承关系复用代码
- 最少知识原则（迪米特法则，Lo**D**）- 不要给没有必然联系的对象发消息

> 说明：上面加粗的字母放在一起称为面向对象的**SOLID**原则。

##### GoF设计模式

- 创建型模式：单例、工厂、建造者、原型
- 结构型模式：适配器、门面（外观）、代理
- 行为型模式：迭代器、观察者、状态、策略

##### 迭代器和生成器

- 和迭代器相关的魔术方法（`__iter__`和`__next__`）
- 两种创建生成器的方式（生成器表达式和`yield`关键字）

```python
def fib(num):
    """生成器"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a
   
   
class Fib(object):
    """迭代器"""
    
    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0
   
    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()
```

参考：[Python yield 使用浅析](https://www.runoob.com/w3cnote/python-yield-used-analysis.html)

##### 并发编程

`Python`中实现并发编程的三种方案：多线程、多进程和异步I/O。并发编程的好处在于可以提升程序的执行效率以及改善用户体验；坏处在于并发的程序不容易开发和调试，同时对其他程序来说它并不友好。

参考：day13对进程和线程进行了说明。

> 进程和线程：
>
> 进程 - 操作系统分配内存的基本单位 - 一个进程可以包含一个或多个线程
> 线程 - 操作系统分配CPU的基本单位
> 并发编程（并发编程）:
> 1。提升执行性能 - 让程序中没有因果关系的部分可以并发的执行
> 2.改善用户体验 - 让耗时间的操作不会造成程序的假死

+ #回忆基础知识

  ```python
  #模拟普通单进程的文件下载
  from time import time, sleep
  from random import randint
  from functools import wraps
  
  def runtime(func):
      '''装饰器：打印函数运行时间'''
      @wraps(func)
      def showtime(*args, **kwargs):
          start = time()
          func(*args, **kwargs)
          end = time()
          print('用时%.2f秒' % (end - start))
      
      return showtime
  
  
  @runtime
  def download(file_name):
      '''下载文件'''
      print('正在下载:%s' % file_name)
      sleep(randint(1, 5)) #随机休眠1~5秒，用来模拟下载过程
  
  @runtime
  def main():
      files = ['jinx.png', 'laozi.txt', 'py.pdf']
      for name in files:
          download(name)
      print('下载完成！总共', end='')
  
  if __name__ == '__main__':
      main()
      
  #运行结果
  '''
  正在下载:jinx.png
  用时1.00秒
  正在下载:laozi.txt
  用时4.00秒
  正在下载:py.pdf
  用时3.01秒
  下载完成！总共用时8.01秒
  '''
  ```

  ```python
  #使用Process类来开启进程
  from time import time, sleep
  from random import randint
  from functools import wraps
  from multiprocessing import Process #导入Process
  
  def runtime(func):
      '''装饰器：打印函数运行时间'''
      @wraps(func)
      def showtime(*args, **kwargs):
          start = time()
          func(*args, **kwargs)
          end = time()
          print('用时%.2f秒' % (end - start))
      
      return showtime
  
  
  @runtime
  def download(file_name):
      '''下载文件'''
      print('正在下载:%s' % file_name)
      sleep(randint(1, 5)) #随机休眠1~5秒，用来模拟下载过程
  
  @runtime
  def main():
      files = ['jinx.png', 'laozi.txt', 'py.pdf']
      ps = []
      for name in files:
          p = Process(target=download, args=(name,)) #1、创建进程
          p.start() #2、开启进程
          ps.append(p)
      
      for pro in ps:
          pro.join()  #3、要求主进程等待子进程的结束
      
      print('下载完成！总共', end='')
  
  if __name__ == '__main__':
      main()
      
  #运行结果  
  '''
  正在下载:laozi.txt
  正在下载:jinx.png
  正在下载:py.pdf
  用时1.00秒
  用时1.00秒
  用时4.00秒
  下载完成！总共用时4.23秒
  '''
  ```

  > 某些多进程之间还需要解决**进程间的通信**问题。

  把多进程改为多线程，我们只需要把Process类换做Thread类即可（虽然使用形式上没啥区别，但处理逻辑却不同）

  ```python
  #使用Process类来开启进程
  from time import time, sleep
  from random import randint
  from functools import wraps
  from threading import Thread #导入Thred
  
  def runtime(func):
      '''装饰器：打印函数运行时间'''
      @wraps(func)
      def showtime(*args, **kwargs):
          start = time()
          func(*args, **kwargs)
          end = time()
          print('用时%.2f秒' % (end - start))
      
      return showtime
  
  
  @runtime
  def download(file_name):
      '''下载文件'''
      print('正在下载:%s' % file_name)
      sleep(randint(1, 5)) #随机休眠1~5秒，用来模拟下载过程
  
  @runtime
  def main():
      files = ['jinx.png', 'laozi.txt', 'py.pdf']
      ps = []
      for name in files:
          p = Thread(target=download, args=(name,)) #1、创建线程
          p.start() #2、开启线程
          ps.append(p)
      
      for pro in ps:
          pro.join() #3、让主进程等待线程的结束
      
      print('下载完成！总共', end='')
  
  if __name__ == '__main__':
      main()
      
  #运行结果  
  '''
  正在下载:jinx.png
  正在下载:laozi.txt
  正在下载:py.pdf
  用时2.00秒
  用时3.00秒
  用时3.00秒
  下载完成！总共用时3.00秒
  '''
  ```

  > 线程之间虽然不需要像进程一样进行通信（处于相同内存区的同一个进程中），但因此也会出现临界资源的争夺问题，所以线程还需要考虑**锁的问题**。

+ #多线程

  Python中提供了`Thread类`并辅以Lock、Condition、Event、Semaphore和Barrier。Python中有GIL来防止多个线程同时执行本地字节码，这个锁对于CPython是必须的，因为CPython的内存管理并不是线程安全的，因为GIL的存在多线程并不能发挥CPU的多核特性。

+ #多进程

  多进程：多进程可以有效的解决GIL的问题，实现多进程主要的类是Process，其他辅助的类跟threading模块中的类似，进程间共享数据可以使用管道、套接字等，在multiprocessing模块中有一个Queue类，它基于管道和锁机制提供了多个进程共享的队列。下面是官方文档上关于多进程和进程池的一个示例。

+ #比较

  > 说明：**多线程和多进程的比较**。
  >
  > 以下情况需要使用多线程：
  >
  > 1. 程序需要维护许多共享的状态（尤其是可变状态），Python中的列表、字典、集合都是线程安全的，所以使用线程而不是进程维护共享状态的代价相对较小。
  > 2. 程序会花费大量时间在I/O操作上，没有太多并行计算的需求且不需占用太多的内存。
  >
  > 以下情况需要使用多进程：
  >
  > 1. 程序执行计算密集型任务（如：字节码操作、数据处理、科学计算）。
  > 2. 程序的输入可以并行的分成块，并且可以将运算结果合并。
  > 3. 程序在内存使用方面没有任何限制且不强依赖于I/O操作（如：读写文件、套接字等）。

+ #异步处理

  从调度程序的任务队列中挑选任务，该调度程序以交叉的形式执行这些任务，我们并不能保证任务将以某种顺序去执行，因为执行顺序取决于队列中的一项任务是否愿意将CPU处理时间让位给另一项任务。异步任务通常通过多任务协作处理的方式来实现，由于执行时间和顺序的不确定，因此需要通过回调式编程或者`future`对象来获取任务执行的结果。Python 3通过`asyncio`模块和`await`和`async`关键字（在Python 3.7中正式被列为关键字）来支持异步处理。

  Python中有一个名为`aiohttp`的三方库，它提供了异步的HTTP客户端和服务器，这个三方库可以跟`asyncio`模块一起工作，并提供了对`Future`对象的支持。Python 3.6中引入了async和await来定义异步执行的函数以及创建异步上下文，在Python 3.7中它们正式成为了关键字。下面的代码异步的从5个URL中获取页面并通过正则表达式的命名捕获组提取了网站的标题。

  > 说明：**异步I/O与多进程的比较**。
  >
  > 当程序不需要真正的并发性或并行性，而是更多的依赖于异步处理和回调时，asyncio就是一种很好的选择。如果程序中有大量的等待与休眠时，也应该考虑asyncio，它很适合编写没有实时数据处理需求的Web应用服务器。

+ #总结

  Python还有很多用于处理并行任务的三方库，例如：joblib、PyMP等。实际开发中，要提升系统的可扩展性和并发性通常有垂直扩展（增加单个节点的处理能力）和水平扩展（将单个节点变成多个节点）两种做法。可以通过消息队列来实现应用程序的解耦合，消息队列相当于是多线程同步队列的扩展版本，不同机器上的应用程序相当于就是线程，而共享的分布式消息队列就是原来程序中的Queue。消息队列（面向消息的中间件）的最流行和最标准化的实现是AMQP（高级消息队列协议），AMQP源于金融行业，提供了排队、路由、可靠传输、安全等功能，最著名的实现包括：Apache的ActiveMQ、RabbitMQ等。

  要实现任务的异步化，可以使用名为Celery的三方库。Celery是Python编写的分布式任务队列，它使用分布式消息进行工作，可以基于RabbitMQ或Redis来作为后端的消息代理。