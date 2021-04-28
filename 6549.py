import sys
input = sys.stdin.readline

# 가로시작,끝으로 탐색
def check(start, end):

    # 시작과끝이 같으면 직사각형 넓이 반환(즉 가로가 1이면)
    if start == end:
        return arr[start]

    # 그게 아니라면 분리시작
    else:
        mid = (start+end)//2
        new_start = mid
        new_end = mid+1
        # 세로값은 생기는 중앙경계의 두값중 작은값으로 설정
        sero = min(arr[new_start], arr[new_end])

        # 1인경우는 고려했으므로 2부터 시작
        garo = 2

        # 경계를 포함하는 네모의 값을 임시 지정
        nemo_temp = sero * 2

        # 경계를 기준으로 네모 확장 시작
        while True:
            # 양쪽 전부 탐색하면 종료
            if (new_start == start) and (new_end == end):
                break

            # 왼쪽 다 탐색시 오른쪽 으로 계속 탐색

            elif new_start == start:
                if arr[new_end+1] < sero:
                    sero = arr[new_end+1]
                new_end += 1
                
            # 오른쪽 다 탐색시 왼쪽 으로 계속 탐색
            elif new_end == end:
                if arr[new_start-1] < sero:
                    sero = arr[new_start-1]
                new_start -= 1

            # 양쪽을 늘릴수 있을때는 한칸씩 비교
            else:
                if arr[new_start-1] > arr[new_end+1]:
                    if arr[new_start - 1] < sero:
                        sero = arr[new_start-1]
                    new_start -= 1
                else:
                    if arr[new_end+1] < sero:
                        sero = arr[new_end+1]
                    new_end += 1

            garo += 1
            nemo_temp = max(nemo_temp, sero * garo)

        # 최종값 출력
        return(max(check(start, mid), check(mid+1, end), nemo_temp))


while True:
    arr = list(map(int, input().split()))

    n = arr[0]
    if n == 0:
        break

    print(check(1, n))
