class Solution(object):
    def twoSum(self, nums, target):
        # l = []
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j :
        #             continue
        #         if nums[i] + nums[j] == target :
        #             l.append(i)
        #             l.append(j)
        #             return l
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, value in enumerate(nums):
            complement = target - value
            
            if complement in nums[i+1:]:
                return nums.index(value), nums[i+1:].index(complement)+i+1
        
        