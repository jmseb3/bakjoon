import sys
n = int(input())

check = [0] *8001
number =[]

for _ in range(n):
    number.append(int(sys.stdin.readline()))

if n ==1:
    print(number[0])
    print(number[0])
    print(number[0])
    print(0)
    exit()

number.sort()

for i in number:
    if i < 0:
        check[4000-(i)] +=1
    else:
        check[i] +=1

print(round(sum(number)/n))
print(number[n//2])
maxlist=[]
max =1
for v,k in enumerate(check):
    if k > max :
        max = k
        maxlist=[]
        if v >4000:
            maxlist.append(-v+4000)
        else:
            maxlist.append(v)
    elif k == max :
        if v >4000:
            maxlist.append(-v+4000)
        else:
            maxlist.append(v)
    else:
        next

if len(maxlist) == 1 :
    print(maxlist[0])
else:
    maxlist.sort()
    print(maxlist[1])
    

print(number[n-1]-number[0])
