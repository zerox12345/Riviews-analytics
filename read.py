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
print('留言數總共有', len(data), '筆')
print('留言的平均長度為', t / count)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('留言長度小於100共有', len(new),'筆')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('留言有good字眼的共有', len(good),'筆')
print(good[0])