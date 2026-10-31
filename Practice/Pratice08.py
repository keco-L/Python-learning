'''
1. 用成员运算符判断子串 `"py"` 是否在 `s` 里面；判断 `"Py"` 是否在 `s` 里面
2. 切片操作：
   - 截取 `Python`（第一个）
   - 从后往前切片，拿到最后 4 个字符
3. 查找：
   - 使用 `find` 找出第二个 `Python` 的起始下标
   - 使用 `index` 在区间 `[0,10]` 查找子串 `"love"`
   - 统计子串 `"Python"` 一共出现多少次（count）
4. 判断：
   - 判断字符串是否以 `I` 开头（startswith）
   - 判断字符串是否以 `!` 结尾（endswith）
5. 替换：把所有的 `Python` 替换成 `Coding`
6. 分割：用逗号 `,` 分割这个字符串，打印分割后的列表
7. 大小写转换：把整个字符串全部转大写、全部转小写分别输出
'''
from tracemalloc import start


s = "I love Python,Python is fun!"
#1
print('py' in s)
print('Py' in s)
#2
print(s[7:13])
print(s[-4:])
#3
print(s.find('Python',13))
print(s.find('love',0,11))
#4
print(s.startswith(('I')))
print(s.endswith('!'))
#5
print(s.replace('Python','Coding'))
#6
print(s.split(','))
#7
print(s.upper())
print(s.lower())