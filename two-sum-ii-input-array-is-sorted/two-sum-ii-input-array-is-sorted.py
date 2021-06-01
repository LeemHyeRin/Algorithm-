class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for k,v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected,k+1) #마지막 인자는 왼쪽 범위 지정
            if i < len(numbers) and numbers[i] == expected:
                return k+1, i+1
                
            
        