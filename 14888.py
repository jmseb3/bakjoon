from itertools import permutations

def answer(number, oper):
    s = number[0]
    total = []
    k=0
    for i in oper:
        for j in i:
            k += 1
            if j == 0:
                s += number[k]
            elif j == 1:
                s -= number[k]
            elif j == 2:
                s *= number[k]
            else:
                if s > 0:
                    s //= number[k]
                else:
                    s = -s
                    s //= number[k]
                    s = -s

        total.append(s)
        k = 0
        s = number[0]
    return max(total), min(total)

n = int(input())

number = list(map(int, input().split()))
operation = list(map(int, input().split()))

oper = []
#  0 1 2 3 > +  - * //

for i in range(4):
    for j in range(operation[i]):
        oper.append(i)

oper = set(permutations(oper, n-1))

max, min = answer(number, oper)
print(max)
print(min)
