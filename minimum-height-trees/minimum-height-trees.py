import collections
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 1:
            return [0]
        #그래프 생성
        graph = collections.defaultdict(list)
        #무방향 그래프이기 때문에, 양방향으로 추가해야함
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        #그래프에서 leaf인 것 찾기 : 노드에 연결된 다른 노드 리스트의 길이가 1인 경우
        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        #leaf 노드 제거하기
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                #제거도 양방향으로 해줘야함
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                #leaf 제거 후, leaf와 이웃했던 node와 연결된 node가 1개뿐이라면
                #해당 neighbor가 leaf이므로, new_leaves에 추가함
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            #새로운 leaves로 갱신
            leaves = new_leaves
        #마지막에는 결국 2개 or 1개의 node 가 담긴 leaves를 return
        return leaves
                