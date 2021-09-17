def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        temp=[]
        for s in skill:
            if s in tree: 
                temp.append(tree.index(s))
            else:
                temp.append(-1)
        print(temp)
        temp =[t if t!=-1 else len(tree) for t in temp]
        print(temp)
        if temp ==sorted(temp):
            answer +=1
    return answer
