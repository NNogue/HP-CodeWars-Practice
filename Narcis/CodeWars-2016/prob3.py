import sys

words = [ x for x in sys.stdin.read().split('\n') if x != '']

num = int(words.pop(0))

words = [words[x] for x in range(num)]

for i in words:
	for j in range(len(i)-1):
		if i[j] == i[j+1]:
			print 'likes',i
			break
	else:
		print 'hates',i