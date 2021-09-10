def solution(n, words):
    visited = []
    for idx,word in enumerate(words):
        if (word in visited) or (visited and visited[-1][-1] != word[0]):
            q,r = divmod(idx,n)
            return [r+1,q+1]
        visited.append(word)

    return [0,0]