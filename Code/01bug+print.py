print("hello world!")
# print("hello world!")
# print("hello world!")
# print("hello world!")
# print("hello world!")
# print("hello world!")
# print("hello world!")
# print("hello world!")

#可以通过debug调试看到程序执行顺序
'''
多行注释用三引号或者三对双引号
'''
"""
三对双引号注释   
"""
#单行注释  ctr+/ 快捷键 添加或者取消注释，使用的是单行注释

#输出函数
print("哈哈""嘿嘿""嘻嘻") #哈哈嘿嘿嘻嘻

print("哈哈","嘿嘿","嘻嘻") #哈哈 嘿嘿 嘻嘻      ,表示是三个句子互相独立 

# sep相当于分隔符的形式
print("哈哈","嘿嘿","嘻嘻",sep=' ') #哈哈 嘿嘿 嘻嘻 
print("哈哈","嘿嘿","嘻嘻",sep='123')#哈哈123嘿嘿123嘻嘻

#end用来设定结尾形式 默认是换行符\n,可以换成其他字符
#print1+end+print2
print("hello world!",end='+')
print("我是Python")        # hello world!+我是Python