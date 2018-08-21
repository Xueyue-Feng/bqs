from collections import Counter, OrderedDict

# 1.交换变量的值
from copy import deepcopy
from operator import itemgetter

a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)

# 2.将列表中的所有元素组合成字符串
a = ["python", "is" ,"awesome"]
print(" ".join(a))

# 3.查找列表中频率最高的值
a = [1, 2, 3, 4, 5, 6, 1, 2, 1, 2, 3, 4, 5, 8, 1]
print(max(set(a), key = a.count))
cnt = Counter(a)
print(cnt.most_common(3))

# 4.检查两个字符串是不是由相同字母不同顺序组成
str1 = "asd"
str2 = "ads"
Counter(str1) == Counter(str2)

# 5.反转字符串
a = 'asdasgjhirljhjqnzjhleojz'
print(a[::-1])

# for  char in reversed(a) :
#     print(char)

num = 123456789
print(int(str(num)[::-1]))

# 6.反转列表
a = [5, 4, 3, 2, 1]
print(a[::-1])

# for ele in reversed(a):
#     print(ele)

# 7.转置二维数组
original = [['a', 'b'],['c', 'd'],['e', 'f']]
transposed = zip(*original)
print(list(transposed))

# 8.链式比较
b = 6
print(4 < b < 7)
print(1 == b < 20)

# 9.链式函数调用
def product(a, b):
    return a * b
def add(a, b):
    return a + b
b = True
print((product if b else add)(5, 7))

# 10.复制列表
a = [5, 4, 3, 2, 1]
# b = a
# b[0] = 10
b = a[:]
b[0] = 10
print(list(b))
print(a.copy())

l = [[1,2],[3,4]]
l2 = deepcopy(l)
print(l2)

# 11.字典 get 方法
d = {'a':1,'b':2}
print(d.get('c', 3))

# 12.通过「键」排序字典元素
d = {'apple': 10, 'orange':20, 'banana':5, 'rotten tomato':1}
print(sorted(d.items(), key=lambda x: x[1]))
print(sorted(d.items(), key=itemgetter(1)))
print(sorted(d, key=d.get))

# 13.for else
a = [5, 4, 3, 2, 1]
for el in a:
    if el == 0:
        break
else:
    print("did not break out of for loop")

# 14.转换列表为逗号分割符格式
items = ['foo', 'bar', 'xyz']
print(','.join(items))

numbers = [2,4,5,6,10]
print(','.join(map(str, numbers)))

data = [2, 'hello', 3, 3.1]
print(' '.join(map(str, data)))

# 15.列表中最小和最大值的索引
lst = [40, 10, 20, 30, 500]

def minIndex(lst):
    return min(range(len(lst)), key=lst.__getitem__)

def maxIndex(lst):
    return max(range(len(lst)), key=lst.__getitem__)

print(maxIndex(lst))
print(minIndex(lst))

# 16.移除列表中的重复元素
items = [2, 2, 3, 1, 1, 5, 6, 4, 3]
newitems2 = list(set(items))
print(newitems2)

items = ["fff","ggg","zoo","fff","ggg"]
print(list(OrderedDict.fromkeys(items).keys()))