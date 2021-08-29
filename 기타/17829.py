import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]


def find_num(row1, row2):
    data = row1+row2
    data.sort()
    return data[-2]


def find_row(maps):
    length = len(maps[0])
    temp =[]
    for x in range(0,length, 2):
        tmp = []
        for y in range(2):
            tmp.append(maps[y][x:x+2])
        temp.append(find_num(tmp[0], tmp[1]))
    return temp


def dfs(maps):
    length = len(maps)
    if length == 2:
        return find_num(maps[0],maps[1])
    res_maps = [[0]*(length//2) for _ in range(length//2)]
    for y in range(0,length, 2):
        res_maps[y//2] = find_row(maps[y:y+2])

    return dfs(res_maps)

print(dfs(arr))


