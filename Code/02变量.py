#1.定义变量的格式：变量名=值
'''
    num1=3
    num2=4
    sum=num1+num2
    print("总价格为：",sum,sep=''); 总价格为：7
    print('你干嘛')
'''

#2.标识符 定义的含义名
'''
规定
  1.只能由数字、字母、下划线组成
  2.不能以数字开头
  eg:
  1uesr=0;   会报错
  3.python可以用中文命名
  4.标识符在括号内对标识符没有影响
    eg:
    (user)=1;
    print(user);   1

  5.不能使用关键字命名 if,else,bool
  6.严格区分大小写
'''

#3.数值类型  检测类型的函数方法 type()
    #3.1整型 int
# num=1
# print(type(num))
    #3.2浮点型 小数
    #3.3bool    true   false
        #true=1   false=0
        # a=True
        # b=False
        # print(a+b)    输出结果1
        # print(type(a))  bool
    #3.4 complex   复数型  固定形式：z=a+bj
        # print(type(2+3j))
        # m1=1+2j
        # m2=2+6j
        # print(m1+m2)
    #3.5字符串 str  
        #a='132'    a="123"   a="""123"""(三引号是多行句子输出）
            # str1="""我是
            # 123
            # 678
            # 对不对"""
            # print(str1)    
            # 我是
            # 123
            # 678
            # 对不对
    
