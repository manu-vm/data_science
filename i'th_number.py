lis = [1,1,1,1,1]
len_lis = len(lis)+1
for i in range(1,len_lis):
	sum_idx = sum(lis[:i])
	if i==sum_idx:
		print(i,True)