# while 循环
'''
a=10
while a>=0 :
    print(a,"我喜欢你")
    a-=1
'''
'''
while '123':
    print("死循环")
'''
#while循环嵌套
'''
num1=1
while num1<=4:
     print(f"外循环{num1}") 
     num2=1
     while num2<=5:
       
         print(f"内循环{num2}")
         num2+=1
     num1+=1

'''
#for 循环
'''
for 临时变量 in 可迭代对象(字符串类型)
str='12xjhs4'
for i in str:
    print(i)

range()计数函数  计数器
range(start,stop,step)
- `start`：起始值，**默认 0**
- `stop`：结束边界（取不到！必填）
- `step`：步长，每次增加多少，**默认 1**
'''
# for i in range(1,6):#从1-6.包前不包后[)
#     print (i)
# for i in range(6):#默认从0开始，6是循环次数
#     print ()
'''
计算1-100的和
sum=0
for i in range(1,101):
    sum+=i
print(sum)'''

#break :中途退出 结束循环 
#continue：结束本次循环，进入下一个循环

'''
i=1
while i<=5:
    print(f"我在吃第{i}个苹果")
    if i==3:
        print("吃饱了")
        break
    i+=1
'''


'''i=1
while i<=5:
    print(f"我在吃第{i}个苹果")
    if i==3:
        print("吃到虫子,第{i}个不吃了")
        i+=1
        continue#跳过后面的 i+=1
    i+=1
'''
'''
for i in range(5):
    if i==3:
        # break
        continue
    print(i)'''