a = int(input())

alpha_list = []
cnt =0
status ="yes"

for i in range(65, 91):
    alpha_list.append(chr(i).lower())

for l in range(a):
    b = input()
    for j in alpha_list:
        temp_list = []
        for num, value in enumerate(b):
            if value == j:
                temp_list.append(num)

        if len(temp_list) > 1:
            for k in range(len(temp_list)-1):
                if temp_list[k+1]-temp_list[k] != 1:
                    status ="no"

    if status =="yes":
        cnt +=1
    
    status ="yes"



print(cnt)