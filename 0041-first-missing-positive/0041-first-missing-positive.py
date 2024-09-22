class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        maxNum = max(nums)
        n = 1
        
        while n <= maxNum:
            if n not in nums:
                return n
            n += 1
        return n