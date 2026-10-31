'''
list1 = [1,3,5,7,9,3,5]
list2 = [2,3,6,7,10,2]
1. 把两个列表转为集合，去除各自重复元素
2. 输出**同时在两个里面都有的元素（交集）**
3. 输出**只在 list1 里存在、list2 没有的元素（差集）**
4. 输出两个集合所有不重复元素合并（并集）
'''
# list1 = [1,3,5,7,9,3,5]
# list2 = [2,3,6,7,10,2]
# len1=len(list1)
# len2=len(list2)
# set1={}
# set1=set()
# set2={}
# set2=set()
# for i in range(len1):
#     set1.add(list1[i])
# for i in range(len2):
#     set2.add(list2[i])
# print("交集为：",set1&set2)
# print("差集为:",set1-set2)
# print("并集为：",set1|set2)

nums = [12, 5, 8, 12, 20, 5, 33, 8, 9]
'''
1. 利用集合，找出这个列表里**一共出现过多少种不同数字**
2. 找出里面大于 10 的不重复数字，保存到集合 `s_gt10`
3. 判断数字 `20` 是否在 `s_gt10` 里面，打印布尔结果
'''
set1=set()
s_gt10=set()
ls=len(nums)
for i in range(ls):
    set1.add(nums[i])
    if nums[i]>10:
        s_gt10.add(nums[i])
if 20 in s_gt10:
    print("True")
else:
    print("False")
print(len(set1))#一共出现过多少种不同数字