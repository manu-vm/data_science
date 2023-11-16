lis = [1,2,10,17]
average = sum(lis)/len(lis)
lis_dev = []
for i in lis:
	dev = (i-average)
	if dev<0:
		dev = dev*-1
	tup = dev,i
	lis_dev.append(tup)
print(lis_dev)
lis_dev.sort()
print(lis_dev)
print(lis_dev[-1][1])