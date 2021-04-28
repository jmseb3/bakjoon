n = int(input())
check_cm =[]
check_kg =[]
grade_total =[]

for i in range(n):
    cm ,kg = map(int,input().split())
    check_cm.append(cm)
    check_kg.append(kg)

for i in range(0,n):
    grade = 1
    for j in range(0,n):
        if check_cm[i]<check_cm[j] and check_kg[i] < check_kg[j]:
            grade +=1
    grade_total.append(grade)

for j in grade_total:
    print(j,end=" ")