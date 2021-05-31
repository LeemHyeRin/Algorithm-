import collections
class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        
        #Q 변수 : (소요시간,정점)
        Q = [(0, k)]
        
        #정점까지 최단거리를 계산하기 위한 dictionary
        dist = collections.defaultdict(int)
        
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                #도착 노드까지 소요시간 누적해서 더해줌
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        
        #모든 노드를 커버한다면
        if len(dist) == n :
            return max(dist.values())
        return -1
                
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #우선 딕셔너리 형태로 그래프 만들기
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))
            
        #큐 변수 : [소요시간, 정점]
        Q = [(0, k)]
        dist = collections.defaultdict(list)
        
        #bfs로 탐색하기
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
                
        if len(dist) == n:
            return max(dist.values())
        
        return -1        
    
    