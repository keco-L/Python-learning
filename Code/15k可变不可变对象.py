#可变类型  list dict set
#变量对应的值可以修改  但是内存地址不发生改变
'''
dic={'name':'lurry','age':18}
print(id(dic))#2487561794624
dic['name']='string'
print(id(dic))#2487561794624
'''
#不可变类型  数值类型、字符串、元组   修改值之后会重新分配内存空间
'''
a=10
print(id(a))#140722335802928
a=5
print(id(a))#140722335802768
'''

# tuan=(1,2,3,4,5)
# print(id(tuan))
# #不支持修改操作
