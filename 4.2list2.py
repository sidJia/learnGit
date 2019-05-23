# in len() sorted(list1)重新排序  append()整体添加 extend()扩展后添加 count() index()
# insert(1,'d')插入  remove('a')删除第一个a reverse()反转 sort()

# list1 = ['a','b','c']
# list2 = [1,2,3]
# list1.sort(reverse=True)
# print(list1)

list1=['t','f','g']
list2=['x','a','s']

list1.extend(list2)
# print(list1)
# print(sorted(list1))
list1.sort(reverse=True)
# print(list1)
print(list1.index('g'))
