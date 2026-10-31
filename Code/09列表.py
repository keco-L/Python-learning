#列表
#基本格式  list a=[1,2,3,4,.....]
#元素之间的数据类型可以各不相同  可以进行切片操作
#可以for循环遍历取值
'''li=[1,2,'a',4]
print((li,type(li)))
print(li[0:3])
for i in li :
    print(i)'''


#列表的常见操作  增删改查
#添加元素  append(str)  extend(str)  insert(插入位置，str)
'''
li=['a','b','c']
li.append('dfd')  #自动填充到最后  整体添加
print(li)
li.extend('ffg')   #分散添加 
print(li)  # ['a', 'b', 'c', 'dfd', 'f', 'f', 'g']
li.insert(1,'lwl')  
print(li) #['a', 'lwl', 'b', 'c', 'dfd', 'f', 'f', 'g']
'''


#修改元素
#直接通过下标进行修改
'''
li=[1,2,3]
li[1]='a'
print(li)   #[1, 'a', 3]

'''
#查询  in  not in 

'''
li=['我是','lwl','yes']
print('lwl' in li)  #True
'''


#案例1  用户输入用户名，昵称重复不能使用

'''
li=['fwx','lwl','yl','ljl']
while True:
    name1=input("请输入昵称：")
    if name1 in li:
      print("重复")
    else:
        li.append(name1)
        print(li)
        break
'''

#查找 index 检测某个子字符串是否在字符串中，如果在就返回这个子字符串开始的下标，否则就会异常
# count 统计出现次数
'''
li=['123','689','sarsa','689']
print(li.index('689'))
print(li.count('689'))
'''

#删除  del

'''
li=['i','love','you']
# del li
# print(li)  #li 已经被删除了
li2=['12','34','56']
del li2[1]
print(li2)  #print(li.index('689'))
'''

#删除 pop  
#删除指定下标的数据，python3版本默认删除最后一个元素
'''
li=['i','love','you']
# li.pop()#默认删除最后一个元素
# print(li)# ['i', 'love']
li.pop(1)
print(li)  #['i', 'you']
'''

#remove
#根据元素的值进行删除

'''
li=['i','love','you','i']
li.remove('i')#默认删除最开始出现的指定元素
print(li)  #li=['love', 'you', 'i']
'''

#排序  sort:从小到大排序  reverse():倒序
'''
li=[1,6,3,8,2,10]
# li.sort()
li.reverse()#[10, 2, 8, 3, 6, 1]
print(li)
'''

#列表推导式
#格式1：[表达式 for 变量 in 列表/range()/可迭代对象]
'''
li=[1,2,34,5,6,7]
# [print(i)for i in li]
#格式1：[表达式 for 变量 in 列表/range()/可迭代对象 if 条件]
[print(i) for i in li if i%2==0]
'''

#列表嵌套
# li=[1,2,[1,3,4],8,9]
# print(li[2][0])