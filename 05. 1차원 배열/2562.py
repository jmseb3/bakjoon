a=[]
for i in range(9):
    a.append(int(input()))

for i ,v in enumerate(a):
    if v == max(a):
        print(v)
        print(i+1)