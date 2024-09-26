class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[n - 2]:
            return n - 1
        
        l, r = 1, n - 2
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            
            if nums[mid - 1] < nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
                
        