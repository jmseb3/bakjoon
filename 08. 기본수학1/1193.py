a = int(input())
sum = 0
i = 0 
num_ans = [0,0]
while sum < a:
    i += 1
    sum += i

cnt = sum - a

if i % 2 == 0 :
    num_ans = [i-cnt,1+cnt]
else:
    num_ans = [1+cnt,i-cnt]

print("{}/{}".format(num_ans[0],num_ans[1]))