#  +  字符串拼接

'''name="lurry"
name_char="性格很好"
print(name+name_char)'''

# *在字符串是重复输出
'''love='我爱你'
print(f'{love}\n'*5)'''

# 成员运算符  检查字符串是否包含某个字符串
'''
in   如果包含返回true,否则返回false
not in   和in相反
'''
'''name='keco'
print('a'in name)  #False
print('c'in name)   #True
print('c'not in name)   #false
print('co' in name) #True
'''

#下标从0开始  进行索引
#格式： 字符串名[下标值]
#从左往右0-   从右往左-1
'''name='i love you'
print(name[0])  #i
print(name[1])   #
print(name[-1])  #u
'''


#切片：对操作的对象截取其中一部分进行操作
#语法：[开始位置：结束位置：步长]  
# 包头不包尾  默认步长为1
#步长绝对值决定切取间隔，-表示从右往左，+表示从左往右
# s='666我服了'
# print(s[5:-4:-1])了服我
'''
st='abcdefg'
print(st[0:1])#a
print(st[3:5])#de
print(st[3:])#defg    下标5之后的都截取到
print(st[:5])#abcde   下标5之前的都截取到
#从右往左进行截取
print(st[-1:])#g
print(st[:-1])#abcdef
print(st[-3:-2])#e    
'''


'''
st='123luowenli' 
#012345678910
print(st[0::4])# 1un 从初始位置开始往右，步长为4进行切割
print(st[10::-3])#ieu2   从初始位置往左
print(st[-1:-8:-2])#inwu
'''

#查找 find()
#检测某个子字符串是否在字符串中，如果在就返回这个子字符串开始的下标，否则就返回-1
'''
#find(str,start,end)
name='123tyu789163'
print(name.find('y',2,6))#4  范围2-6范围寻找
print(name.find('yu',0,9)) #4
print(name.find('23',1))# 从1往后找
print(name.find('23'))# 从0 开始遍历'''


#index(value，start，end)
# 检测某个子字符串是否在字符串中，如果在就返回这个子字符串开始的下标，否则就会异常
'''name="你已急哭"
print(name.index('急'))
print(name.index('急',0,3))
print(name.index('急',-1,-3))#报错  查找是从左往右进行查找
# print(name.index('oo'))#直接报错'''


#count()
#返回某个子字符串在字符串中出现的次数，没有则返回0
#包前不包后
'''
name='2006nian'
print(name.count('0'))#2
print(name.count('n',0,7))#1
print(name.count('n',0,3))  #0
'''

#startswith()判断是否以某个字符开头，是的话返回true,不是的话返回false
'''
name='i am lisa'
print(name.startswith('a',0,)) #False
print(name.startswith('m',3,4))#True
'''

#enswith()判断是否以某个字符结尾，是的话返回true,不是的话返回false

#isupper()检测字符串中的字符是否都是大写
'''name='ASD'
print(name.isupper())
print(name.islower())'''


#replace(旧内容，新内容，替换次数)替换  替换次数不写 就会全部替换
'''name='好好学习，天天向上'
print(name.replace('好','6',1))#6好学习，天天向上
print(name.replace('好','6',2))#66好学习，天天向上'''

#split():指定分割符分割字符
#split('指定的分割符','分割次数')
#如果字符串中不包含分割内容，就不进行分割
'''name='hello,world'
print(name.split(','))#['hello', 'world']
name1='hello,world'
print(name1.split('.'))#['hello,world']  没有进行分割
print(name1.split('o',2))#['hell', ',w', 'rld']  以O分割了两次'''


#capitalize():第一个字符大写，其他都是小写
'''name='AAALaoDa'
a=name.capitalize()
print(a)#Aaalaoda'''


#lower()   upper()
# name='abcdFTRUS'
# print(name.lower())  #abcdftrus
# print(name.upper())  #ABCDFTRUS