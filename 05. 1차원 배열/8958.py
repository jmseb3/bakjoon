t = int(input())
for i in range(t):
    score = 0
    sum =0
    a = input()
    for b in a:
        if b =="O":
            score +=1
            sum +=score
        else:
            score =0
    print(sum)