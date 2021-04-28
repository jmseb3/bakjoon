case = int(input())

for _ in range(case):
    function = list(input())
    num = int(input())
    arr = eval(input())
    error = False
    R_count = 0 #홀/짝 뒤집힌 횟수용
    D_front = 0 #앞에서 없어지는 수
    
    for func in function:            
        if func == 'R':
            R_count += 1
        else:
            try:
                if R_count % 2 == 0:
                    D_front += 1 #앞에서는 슬라이싱으로 나중에 뺴줌
                else:
                    arr.pop() #이건 뒤에서 바로 뺴줌
            except:
                error = True
                break
                
    #에러 걸러주기
    if error or D_front > len(arr):
        print('error')
        continue
        
    #R개수에 따른 정답 변형
    if R_count % 2 == 0:
        answer = arr[D_front:]
    else:
        answer = list(reversed(arr[D_front:]))
        
    #출력함수
    print("[", end='')
    print(*answer,sep=',',end="")
    print("]")