class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        graph = collections.defaultdict(list)
        route = []
        # recursion 이용
        '''
        for a,b in sorted(tickets):
            graph[a].append(b)

        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop(0))
            route.append(start)
        
        dfs('JFK')
        
        return route[::-1]
        '''
        
        #재귀 연산 최적화 --> pop() 연산으로 시간 단축
        '''
        for a,b in sorted(tickets, reverse=True):
            graph[a].append(b)
            
        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())
            route.append(start)
        
        
        dfs('JFK')
        return route[::-1]
        '''
        # stack 이용
        for a,b in sorted(tickets):
            graph[a].append(b)
        
        route = []
        stack = ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
        
        return route[::-1]
            
                
            
        
        