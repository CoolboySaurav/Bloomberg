class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[0] * i for i in range(1, numRows + 1)]
        res[0][0] = 1
        
        
        for i in range(1, numRows):
            for j in range(i + 1):
                right_up = left_up = 0
                if j > 0:
                    left_up = res[i - 1][j - 1]
                if j < i:
                    right_up = res[i - 1][j]
                res[i][j] = left_up + right_up
        return res
                    