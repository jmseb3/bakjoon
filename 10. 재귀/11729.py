def hanoi(disk, start, end):
    if disk == 1:
        print(start, end)
    else:
        hanoi(disk-1, start, 6-start-end)
        print(start, end)
        hanoi(disk-1, 6-start-end, end)


n = int(input())

print(2**n-1)
hanoi(n,1,3) 
