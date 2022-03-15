data = []
count = 0
i = 0
t = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		t = t + len(data[i])
		count += 1
		i += 1
print('留言的平均長度為' t / count)
		
