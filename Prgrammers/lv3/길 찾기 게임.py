import sys
sys.setrecursionlimit(10**6)


class Tree:
    def __init__(self, datalist):
        self.data = max(datalist, key=lambda x: x[1])
        leftlist = list(filter(lambda x: x[0] < self.data[0], datalist))
        rightlist = list(filter(lambda x: x[0] > self.data[0], datalist))

        if leftlist != []:
            self.left = Tree(leftlist)
        else:
            self.left = None

        if rightlist != []:
            self.right = Tree(rightlist)
        else:
            self.right = None


def solution(nodeinfo):
    def fix(root,post,pre):
        post.append(root.data)
        if root.left != None:
            fix(root.left,post,pre)
        
        if root.right != None:
            fix(root.right,post,pre)
        pre.append(root.data)
    answer = []
    root = Tree(nodeinfo)
    post, pre = [], []
    fix(root, post, pre)
    answer.append((list(map(lambda x: nodeinfo.index(x)+1,post))))
    answer.append((list(map(lambda x: nodeinfo.index(x)+1,pre))))
    return answer
