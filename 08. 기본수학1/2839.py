n = int(input())
i = n //5
result = -1
while i >=0 :
    n_2 = n- 5*i
    if n_2 % 3 == 0:
        result = int(i + n_2/3)
        break
    else:
        i -= 1

print(result)