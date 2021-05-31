class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #dfs 구조 사용할 것
        #재귀를 이용할 것
        def dfs(index, path):
            result.append(path)
            
            for i in range(index, len(nums)):
                dfs(i + 1, path+[nums[i]])
            
        result = []
        dfs(0, [])
        return result