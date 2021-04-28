import sys

n = int(input())
number =[]

for _ in range(n):
    number.append(int(sys.stdin.readline()))

number.sort()

ans =""
for i in number:
    ans +=str(i)+"\n"

sys.stdout.write(ans)