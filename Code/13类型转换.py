#类型转化  
#int()转化为一个整数  只能转化由纯数字组成的字符串
'''
str='123456'
print(type(int(str)))#<class 'int'>
a=6.64
print(int(a))#6  浮点数强制转换为整型，只保留整数部分
#如果字符串中有除了数字和+-之外的字符，就会发生报错
print(int('-10'))
'''
#案例1    
# age=input("请输入年龄")
# if age>=18:
#     print("成年了")
#会报错 因为input()默认输入的是字符串类型
#修正：
# age=input("请输入年龄")
# if int(age)>=18:
#     print("成年了")




#float()：转化为一个小数
 #如果字符串中除了正负号、数字和小数点之外的字符，暂不支持转换
# print(float(11))#11.0   整型转换为浮点型会自动添加一位小数
# print(float(11.345)) 



#str():任何类型都可以转换
# a=100
# print(str(a))
# print(str(1.00))#1.0  浮点数转换为str会去除末尾为0的小数部分
# li=[1,2,3]
# print(str(li))

#eval():执行运算并返回运算的值  对List,dict,str,tuple之间的一个转换
# s1 = "[1,2,3]"           # Python列表表达式 → eval得到 list
# s2 = "[1,2,3],[4,5]"     # 逗号隔开，无外层[] → 元组 tuple
# s3 = "100"               # 得到整数
# s4 = "{'a':1}"           # 得到字典

'''
print(10+10)  #20
print('10+10')
# print(int('10+10'))#报错   +号不在最前面
print(eval('10+10'))  #20  
print(eval('10'+'10'))#1.0
str='[1,2,3],[2,3,4],[5,6,7]'
li=eval(str)    #转换为了元组
print(li)  #([1, 2, 3], [2, 3, 4], [5, 6, 7])
dic="{'a':1}"
dicc=eval(dic)
print(dicc)
'''

#list():将可迭代对象（字符串、元组、字典、集合）转换为列表
'''
str1="我爱你"
list1=list(str1)
print(list1)  #['我', '爱', '你']
tuan1=(1,2,3,4)
print(list(tuan1))#[1, 2, 3, 4]
dic={'w':12,'y':19,'z':31}
print(list(dic))#['w', 'y', 'z']   字典转换为列表，取得是键名
set1={1,2,'str','who'}
print(list(set1))#['str', 1, 2, 'who']   集合转换欸列表，先去重再转换
'''

