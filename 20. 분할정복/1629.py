import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())
ans = 1


def answer(a, b, c):
    global ans
    # b가 1이라면 답을 출력하고 종료
    if b == 1:
        print((a*ans) % c)
        return

    # b가 홀수라면 답에a를 곱해둠
    if b % 2 == 1:
        ans *= a
    
    # 그다음으로 a^2하고 b//2해서 진행
    answer((a*a) % c, b//2, c)

answer(a,b,c)