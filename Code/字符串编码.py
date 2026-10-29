#字母是一个字节  汉字一般是占据3个字节
#Unicode：所有字符都是两个字节  有一些浪费空间，但是字符之间的转换会快一些
#UTF-8 不同字符的长度不一样，不浪费空间，但是转换麻烦一些
'''
encode()编码
decode()解码
'''

#1.字符串编码转化
a='hello'
print(a,type(a))#str   #字符为单位进行存储
a1=a.encode()
print("编码之后：",a1)
print(type(a1))#byte  字节为单位进行存储
a2=a1.decode()
print(a2,type(a2))