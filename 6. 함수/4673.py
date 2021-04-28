
def kaprekar(n):
    num = n
    while True:
        if n >= 10:
            num += n % 10
            n = n//10
            else:
                num += n
                break
            
        return num


num_list = []

for i in range(10000):
    num_list.append(kaprekar(i))


ans_list = list(set(range(10000)) - set(num_list))
ans_list.sort()


for ans in ans_list:
    print(ans)

