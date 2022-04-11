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

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('留言長度小於100共有', len(new),'筆')
new = [d for d in data if len(d) < 100]
print('留言長度小於100共有', len(new),'筆')

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('留言有good字眼的共有', len(good),'筆')
good = [d for d in data if 'good' in d]
print('留言有good字眼的共有', len(good),'筆')

#文字計數
wc = {}
for line in data:
	words = line.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

while True:
	word = input('what!?\n')
	if word == 'q':
		break
	if word in wc:
		print(word, wc[word])
	else:
		print('Not found in wc')

print('Thanks for applying')
