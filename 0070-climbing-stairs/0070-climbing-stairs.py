class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev2 = 0
        prev1 = 1
        
        for i in range(1, n + 1):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur
        return prev1
        
        
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            cur = 0
            if i > 1:
                cur += dp[i - 2]
            cur += dp[i - 1]
            dp[i] = cur 
        return dp[n]
            
        dp = [-1] * (n + 1)
        def helper(num):
            if num < 0:
                return 0
            if num == 0:
                return 1
            if dp[num] != -1:
                return dp[num]
            dp[num] = helper(num - 1) + helper(num - 2)
            return dp[num]
        
        return helper(n)