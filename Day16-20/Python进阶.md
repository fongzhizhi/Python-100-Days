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

