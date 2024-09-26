class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        prev=[1]*n

        for i in range(1,m):
            temp=[0]*n
            for j in range(n):
                up=left=0
                up=prev[j]
                if j>0:
                    left=temp[j-1]
                temp[j]=up+left
            prev=temp
            
        return prev[n-1]

        
        
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                up = left = 0
                if i == j == 0:
                    continue
                if i > 0:
                    up = dp[i - 1][j]
                if j > 0:
                    left = dp[i][j - 1]
                dp[i][j] = up + left 
        return dp[m - 1][n - 1]
        
        
        dp = [[-1] * n for _ in range(m)]
        
        def helper(i, j):
            if i < 0 or j < 0:
                return 0
            if i == j == 0:
                return 1
            if dp[i][j] != -1:
                return  dp[i][j]
            up = helper(i - 1, j)
            left = helper(i, j - 1)
            dp[i][j] = up + left
            return dp[i][j]
        
        
        return helper(m - 1, n - 1)