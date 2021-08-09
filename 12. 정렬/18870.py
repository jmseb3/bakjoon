import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
sort_arr=sorted(set(arr))
arr_dict={i:v for v,i in enumerate(sort_arr)}
for i in arr:
    print(arr_dict[i],end=" ")
