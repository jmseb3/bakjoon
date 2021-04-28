import sys
n = int(input())
user=[]
for j in range(n):
    age,name = map(str,sys.stdin.readline().split())
    user.append([int(age),j,name])

user.sort()
for j in range(n):
    print(user[j][0],user[j][2])
