dict1 = {'name':'kylin','age':12}
# print(dict1)
list1=[[1,'a'],[2,'b']]
dict2=dict(list1)
# print(dict2)

print(dict1['name'])

scores={'math':98,
       'english':92,
       'chinese':80,
       'PE':'A'
       }
print(scores)
scores['math']=95
print(scores)
scores['sci']=100
print(scores)
del scores['sci']
print(scores)

list1={'breakfast':'noodles',
       'lunch':'chicken',
       'dinner':'rice'
       }
print(list1)
list1['snack']='dumplings'
print(list1)