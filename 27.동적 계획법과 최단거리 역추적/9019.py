from collections import deque
T = int(input())

for _ in range(T):
    commands = ['D', 'S', 'L', 'R']
    a, b = map(int, input().split())
    visited = [False]*10000
    visited[a] = True
    q = deque([(a, '')])
    while q:
        now, path = q.popleft()
        if now == b:
            print(path)
            break
        d = (now * 2) % 10000
        s = now - 1 if now != 0 else 9999
        l = (now*10 + now//1000) % 10000
        r = (now+(now % 10)*10000)//10
        for nums,paths in zip([d,s,l,r],commands):
            if not visited[nums]:
                q.append((nums,path+paths))
                visited[nums] = True

