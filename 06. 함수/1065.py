def hansu(n: int) -> int:
    if n >=100:
        num_list=[]
        while True:
            if n >= 10:
                num_list.append(n % 10)
                n = n//10
            else:
                num_list.append(n)
                break
        
        num2_list=[]
        cnt = len(num_list)
        for j in range(cnt-1):
            num2_list.append(num_list[j]-num_list[j+1])
        
        if len(set(num2_list)) == 1:
            return 1
        else:
            return 0
    else:
        return 1

n= int(input())
sumn = 0
for i in range(1,n+1):
    sumn += int(hansu(i))
print(sumn)