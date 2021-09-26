T = input()
P = input()

table = [0 for _ in range(0, len(P))]
j = 0
for i in range(1, len(P)):
    while j > 0 and P[i] != P[j]:
        j = table[j - 1]

    if (P[i] == P[j]):
        j += 1
        table[i] = j

result = []
count = 0

j = 0
for i in range(0, len(T)):

    while j > 0 and T[i] != P[j]:
        j = table[j - 1]

    if T[i] == P[j]:
        if j == (len(P) - 1):
            result.append(i - len(P) + 2)
            count += 1
            j = table[j]
        else:
            j += 1

print(count)
for element in result:
    print(element)
