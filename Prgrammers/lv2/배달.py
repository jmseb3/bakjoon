from collections import defaultdict
import heapq

def solution(N, road, K):
    INF = int(1e9)
    graph = defaultdict(list)
    road.sort()
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    distance =[INF] *(N+1)
    
    def dijkstra(start):
        distance[start] = 0
        q = []
        heapq.heappush(q, (0, start))
        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue
            for next, next_dist in graph[now]:
                cost = dist+next_dist
                if cost < distance[next]:
                    distance[next] = cost
                    heapq.heappush(q, (cost, next))
    dijkstra(1)
    answer = 0
    for x in distance:
        if x <=K:
            answer +=1

    return answer
