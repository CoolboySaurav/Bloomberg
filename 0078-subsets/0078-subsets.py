class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def helper(ind, path):
            if ind == len(nums):
                res.append(path)
                return None
            
            helper(ind + 1, path + [nums[ind]])
            helper(ind + 1, path)
        
        helper(0, [])
        return res