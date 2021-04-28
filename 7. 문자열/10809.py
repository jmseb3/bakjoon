s = list(input())
alp ={}
for i in range(97, 123, 1) :
    alp[chr(i)] = -1

for v, k in enumerate(s):
    if alp[k] == -1:
        alp[k] = v
    
for v in alp.values():
    print(v,end=" ")