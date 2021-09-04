import sys
input = sys.stdin.readline

# 세그먼트 트리 만들기


def init(start, end, node):
    if start == end:
        tree[node] = array[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]

# 구간 합 구하기


def summit(start, end, node, left, right):
    # left 와 right가 범위에서 벗어났기 떄문에 return
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start+end) // 2
    return summit(start, mid, node*2, left, right) + summit(mid + 1, end, node*2+1, left, right)

# 특정 인덱스 값 바꾸기


def update(start, end, node, index, dif):
    if index < start or index > end:
        return

    tree[node] += dif
    if start == end:
        return

    mid = (start+end) // 2
    update(start, mid, node*2, index, dif)
    update(mid+1, end, node*2+1, index, dif)


N, M, K = map(int, input().rstrip().split())

array = []
tree = [0] * ((4*N))

for i in range(N):
    array.append(int(input().rstrip()))

init(0, N-1, 1)
print(tree)

for i in range(M+K):
    cmd = list(map(int, input().rstrip().split()))

    if cmd[0] == 1:
        cmd[1] -= 1
        diff = cmd[2] - array[cmd[1]]
        array[cmd[1]] = cmd[2]
        update(0, N-1, 1, cmd[1], diff)
    elif cmd[0] == 2:
        print(summit(0, N-1, 1, cmd[1]-1, cmd[2]-1))
