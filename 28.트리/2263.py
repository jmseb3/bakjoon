import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

idx = [0]*(N+1)

for i in range(N):
    idx[inorder[i]] = i

def dfs(l,r,left_pos,right_pos):
    if l>r or left_pos > right_pos:
        return
    
    parent = postorder[right_pos]
    print(parent, end=" ")
    Sidx = idx[parent]
    left = Sidx - l

    dfs(l,Sidx-1,left_pos,(left_pos+left)-1)
    dfs(Sidx+1,r,left_pos+left,right_pos-1)

dfs(0,N-1,0,N-1)