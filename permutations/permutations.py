class Solution(object):
    def permute(self, nums):
        result = []
        prev_elements = []
        '''
        def dfs(elements):
            #leaf node일 때 결과를 추가
            if len(elements) == 0:
                result.append(prev_elements[:])
            
            #순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
                
        dfs(nums)
        return result
        '''
        return list(itertools.permutations(nums))