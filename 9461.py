n = int(input())
check =[0]*101
check[1:8] = [1,1,1,2,2,3,4,5]

for j in range(9,101):
        check[j] += check[j-1] + check[j-5]

for _ in range(n):
    print(check[int(input())])