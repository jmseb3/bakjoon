import sys
input = sys.stdin.readline

N = int(input())


def prime():
    result = []
    data =[True for _ in range(N+1)]
    for i in range(2, int(N**0.5)+1):
        if data[i]:
            for j in range(i+i, N+1, i):
                data[j] = False

    for i in range(2, N+1):
        if data[i]:
            result.append(i)
    return result
def soluton(N):
    if N==1:
        return 0
    prime_list = prime()
    length = len(prime_list)
    sum_arr = [0 for _ in range(length)]
    sum_arr[0] = prime_list[0]

    for idx in range(1, length):
        sum_arr[idx] = sum_arr[idx-1] + prime_list[idx]
    cnt, start, end = 0, 0, 0

    while start<=end:
        if end ==length:
            break
        ck = sum_arr[end]-sum_arr[start-1] if start != 0 else sum_arr[end]
        
        if ck >=N:
            if ck ==N:
                cnt +=1
            start+=1
        else:
            end +=1
    
    return cnt

print(soluton(N))