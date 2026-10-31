#字典dict  格式：dic={键：值1，2，3，}
#键与值之间用：隔开    键值对之间用，隔开
#字典中没有下标 查找元素用键名
# dic={'age':18,'name':'lurry',}
# print(type(dic))
# print(dic['age'])  #18
'''
#查找2  变量名.get('键名')
print(dic.get('name')) #lurry
print(dic.get('sex')) #None  没有就返回none
print(dic.get('sex','不存在'))  #不存在

'''

#修改元素
'''
dic={'age':18,'name':'lurry',}
dic['age']=22
print(dic['age']) #22
'''
#添加元素  dic[键名]=值
#键名存在就修改  不存在就新增
'''
dic={'age':18,'name':'lurry',}
dic['sex']='男'
print(dic)  #{'age': 18, 'name': 'lurry', 'sex': '男'}  没有的话就新增
dic['sex']='女'
print(dic)#{'age': 18, 'name': 'lurry', 'sex': '女'}   有的话就修改
'''

#删除元素

#1.del
# dic={'age':18,'name':'lurry'}
# del dic['age']  如果键名不存在 就会报错
# print(dic)  #{'name': 'lurry'}
# del dic['sex']
# print(dic)
# del dic  #直接清空了dic这个字典
# print(dic)  #dic被删除 找不到了 会报错

#2.clear():清空字典数据 但是字典依然保留

# dic={'age':18,'name':'lurry'}
# dic.clear()
# print(dic) #{}
# dic['sex']='female'
# print(dic) #{'sex': 'female'}

#3.pop():删除指定键值对
'''
dic={'age':18,'name':'lurry'}
# dic.pop('age')
# print(dic)  #{'name': 'lurry'}
dic.popitem()  #默认删除最后一个
print(dic,sep='--')
'''

#len()求长度
'''
dic={'age':18,'name':'lurry'}
li=[1,2,3,4,5]
tuan=(1,2,3)
s1='123456789'
print(len(dic))   #2
print(len(li))  #5
print(len(tuan))  #3
print(len(s1))   #9
'''
#keys()返回字典里面包含的所有键名
'''
dic={'age':18,'name':'lurry'}
print(dic.keys()) #dict_keys(['age', 'name'])
# for i in dic.keys():
#     print(i)        #循环取出键名
'''

#values()返回字典里面包含的所有值
'''
dic={'age':18,'name':'lurry'}
print(dic.values())  #dict_values([18, 'lurry'])
for i in dic.values():
    print(i)
'''

#items()返回字典里面所有的键值对  以元组形式
'''
dic={'age':18,'name':'lurry'}
print(dic.items()) #dict_items([('age', 18), ('name', 'lurry')])
for i in dic.items():
    print(i)  #('age', 18)    ('name', 'lurry')
'''