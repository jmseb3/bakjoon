import sys
n = int(input())
words = []
for _ in range(n):
    temp = sys.stdin.readline().strip()
    if [len(temp),temp] in words:
        next
    else:
        words.append([len(temp),temp])

words.sort()

for j in range(len(words)):
    print(words[j][1])
