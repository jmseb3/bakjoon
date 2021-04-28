def stars(n):
    matix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matix.append(n[i%len(n)] *3)
    return (list(matix))

n = int(input())

star =["***","* *","***"]
k=0
while n !=3:
    n = int(n/3)
    k +=1

for _ in range(k):
    star = stars(star)

for j in star:
    print(j)
