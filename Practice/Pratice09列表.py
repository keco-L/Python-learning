'''
写一个函数 `merge_list(a, b)`，接收两个长度不一定相等的列表，按**交错方式合并**：依次取 a [0], b [0], a [1], b [1]……
如果其中一个列表先取完，把剩下的元素直接追加到末尾。
'''
# lia=[1,2,3,4,5,7,8,9]
# lib=['a','b','c','d']
# def merge_list(a, b):
#   res = []
#   max_len = max(len(a), len(b))
#   for i in range(max_len):
#         if i < len(a):
#             res.append(a[i])
#         if i < len(b):
#             res.append(b[i])
#   return res
# print(merge_list(lia,lib))


'''
给定一个整数列表 `nums`，列表里有重复元素，请编写函数：
1. 返回一个新列表，**保留元素第一次出现的顺序**，去掉重复值
2. 同时返回一个字典，记录每个元素一共出现多少次
'''
# ''
# nums = [2,5,2,8,5,9,2]
# def get(a):
#     dic={}
#     for i in range(len(a)):
#         dic[a[i]]=a.count(a[i])
#     for i in range(len(a)):
#         if i>=len(a):
#             break
#         for j in range(len(a)-1,i,-1):
#             if a[j]==a[i]:
#                 del a[j]
#     print(a)
#     print(dic)
# get(nums)
''