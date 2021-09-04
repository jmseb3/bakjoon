import sys
input = sys.stdin.readline

M = int(input())

S = set()

for _ in range(M):
    qry = list(map(str, input().rstrip().split()))

    if qry[0] == "all":
        S = set(list(range(1, 21)))
    elif qry[0] =="empty":
        S.clear()
    else:
        com ,num = qry
        num = int(num)
        if com == "add":
            S.add(num)
        elif com == "remove":
            S.discard(num)
        elif com == "check":
            print(1 if num in S else 0)
        elif com == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)
