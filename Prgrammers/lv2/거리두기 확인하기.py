from collections import deque


def solution(places):
    answer = []
    for place in places:
        ck = True
        for y in range(5):
            if not ck:
                break
            for x in range(5):
                if place[y][x] == 'P':
                    if not check(y, x, place):
                        ck = False
                        break

        if ck:
            answer.append(1)
        else:
            answer.append(0)
    return answer


def check(y, x, arr):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    real = [
        [(-2, 0), (-1, 1), (-1, -1)],
        [(0, 2), (1, 1), (-1, 1)],
        [(2, 0), (1, -1), (1, 1)],
        [(0,-2),(1,-1),(-1,-1)]
    ]
    next_ck =set()
    for idx in range(4):
        ny = y+dy[idx]
        nx = x+dx[idx]
        if ny < 0 or nx < 0 or nx >= 5 or ny >= 5:
            continue
        if arr[ny][nx] == 'P':
            return False
        if arr[ny][nx] == 'X':
            continue
        if arr[ny][nx] == 'O':
            next_ck.update(real[idx])
    
    for dy,dx in next_ck:
        ny = y+dy
        nx = x+dx
        if ny < 0 or nx < 0 or nx >= 5 or ny >= 5:
            continue
        if arr[ny][nx] == 'P':
            return False
        if arr[ny][nx] == 'X':
            continue
        if arr[ny][nx] == 'O':
            continue

    return True

