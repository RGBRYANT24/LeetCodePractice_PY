import collections
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
a.append(0) # 头尾增加0 方便数组处理
a.insert(0, 0)
n += 2
d = defaultdict(list)
def count_para():
	res = 0
	flag = False
	for i in range(n):
		if flag and a[i] != 0: #当前是非0段
			continue
		elif a[i] != 0: # 不满足flag就说明是起点
			flag = True
			res += 1
		elif a[i] == 0:
			flag = False
			continue
	return res


for i in range(n):
	d[a[i]].append(i) # 每一个key对应的数组下标

res = 0
for i in range(n - 2):
	if a[i] == 0 and a[i + 1] != 0:
		res += 1 

res = count_para()
k = list(d.keys())
k.sort()
ans = res
for i in range(len(k)):
	if k[i] == 0:
		continue
	for j in d[k[i]]: # 遍历每一个值为k[i]的数组下标
		if a[j - 1] > 0 and a[j + 1] > 0: # 注意这里一定是左右不为0就行 如果是左右比中间大， 那么20 10 10 15这种情况删除10不会计数
			res += 1# 段数 + 1
		elif a[j - 1] == 0 and a[j + 1] == 0:
			res -= 1
		a[j] = 0
		# print(a, res)
	ans = max(res, ans)

print(ans)


'''n = int(input())
a = [0]+list(map(int, input().split()))+[0]
seta = sorted(set(a))
dic = {}
# dic 中存放的是每个值 和其出现的下标
for i in range(1, n+1):
    if a[i] in dic:
        dic[a[i]].append(i)
    else:
        dic[a[i]] = [i]
pri = 0
num = 0
for i in range(n):
    if a[i] == 0 and a[i+1] != 0:
        num += 1
for key in seta:
    if key == 0:
        continue
    for index in dic[key]:
        a[index] = 0
        if a[index-1] > 0 and a[index+1] > 0:
            num += 1
        elif a[index-1] == 0 and a[index+1] == 0:
            num -= 1
    pri = max(pri, num)
print(pri)'''

		
			
		
	

		