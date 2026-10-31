'''
给定字典 `score = {"小明":88, "小红":92, "小刚":59, "小丽":76, "小华":95}`
要求：
1. 新建一个字典，只保留分数 >=80 的同学
2. 打印新字典
3. 算出这些及格（≥80）同学的平均分，保留 1 位小数
'''
score = {"小明":88, "小红":92, "小刚":59, "小丽":76, "小华":95}
dic={}
l1=len(score)
sum=0
# for n,s in score.items():
#     if s<80:
#         score.pop(n)
# print(score)     迭代过程中字典大小被改变，不允许！
for name,s in score.items():
    if s>=80:
       dic[name]=s
       sum+=s
print(dic)
l2=len(dic)
print("平均数：%.1f"%(sum/l2))


