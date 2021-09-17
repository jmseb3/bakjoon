def solution(sticker):
    N = len(sticker)
    # 3개 이하인경우 제일 큰값
    if N<=3:
        return max(sticker)
    # 첫번째 스티커를 뜯는경우 ->마지막 사용 불가
    dp1 = [0] * (N-1)
    dp1[0] = sticker[0]
    dp1[1] = dp1[0]
    for idx in range(2, N-1):
        dp1[idx] = max(sticker[idx]+dp1[idx-2], dp1[idx-1])
    # 첫번째 스티커를 뜯지 않는경우 -> 마지막 사용가능
    dp2 = [0] * N
    dp2[0] = 0
    dp2[1] = sticker[1]
    for idx in range(2, N):
        dp2[idx] = max(sticker[idx]+dp2[idx-2], dp2[idx-1])

    return max(dp1[-1],dp2[-1])
