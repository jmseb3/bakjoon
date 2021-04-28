a = input()
timelist =[]

def change_time(n):
    temp = int(ord(i))-65
    if temp >= 22:
        return 10
    elif temp >= 19:
        return 9
    elif temp >= 15:
        return 8
    elif temp >= 12:
        return 7
    elif temp >= 9:
        return 6
    elif temp >= 6:
        return 5
    elif temp >= 3:
        return 4
    else:
        return 3

for i in a:
    timelist.append(change_time(i))

print(sum(timelist))