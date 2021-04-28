x, y, w, h = map(int, input().split())
ans_list =[w-x,x,h-y,y]
print(min(ans_list))