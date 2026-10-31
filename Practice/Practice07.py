'''
1. 使用循环，打印 1～20 之间所有**不是 3 的倍数**的数字；
2. 当数字等于 17 的时候，直接结束整个循环；
3. 要求：必须用到 `continue` 和 `break`。
'''
for i in range(1,21):
    if i%3==0:
        continue
    if i==17:
        break
    print(i)
