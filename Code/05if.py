#01  
'''
if 条件:
    （有缩进才行）
'''
# age=18
# if age<18:
#     print('未成年不能上网')
# else:
#     print('成年能上网')


#2.比较运算符
'''
== 、！=、>=、<=
'''
#3.比较运算符
'''
and  左右两边都符合为true
or   左右两边一边符合为true
not  相反的结果
print(not 3>9)  #true
'''
# print(not 3>9)  #true

#4.三目运算  （三元表达式）
# 4.1  
# 基本格式：真结果 if 判断条件 else 假结果
#if 条件：
    # 结果1
# else：
    # 结果2
# num1=100
# num2=98
'''
if num1>num2:
    print("你好")
else:
    print("不好")
'''
# print("你好")if num1>num2 else  print("不好")

#if-elif  多选1
#if-elif-else  else其他都无效的情况
'''
if num1>num2:
    print("你好")
elif num1==num2:
    print("我好")
elif num2>num1:
    print("大家好")
else:
    print("666")
'''
#if 嵌套
age=20
num1=210
num2=200
if num1>num2:
    print("我有钱")
    if age>18:
        print("我有18岁")
    elif age<18:
        print("我没有18岁")
    else:
        print("我刚好18岁")
else:
    print("我也没有钱")