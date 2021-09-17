def solution(record):
    names = {}
    answer = []
    for rec in record:
        opers = rec.split(' ')
        if opers[0] == "Enter":
            names[opers[1]] = opers[2]
            answer.append((opers[1], "님이 들어왔습니다."))
        if opers[0] == "Leave":
            answer.append((opers[1], "님이 나갔습니다."))
        if opers[0] == "Change":
            names[opers[1]] = opers[2]
    res =[names[a]+b for a,b in answer]
    return res


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
      "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
