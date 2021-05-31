class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def dfs(path, csum, index):
            if csum < 0:
                return
            
            if csum == 0:
                result.append(path)
                return
            
            for i in range(index,len(candidates)):
                dfs(path + [candidates[i]], csum - candidates[i] , i)
                   
        
        result = []
        dfs([], target, 0)
        
        return result
            
                
                