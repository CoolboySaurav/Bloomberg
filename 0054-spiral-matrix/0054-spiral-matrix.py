class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])
        l, r = 0, n - 1
        u, d = 0, m - 1
        res = []
        
        while l <= r and u <= d:
            for i in range(l, r + 1):
                res.append(matrix[u][i])
            u += 1
            for i in range(u, d + 1):
                res.append(matrix[i][r])
            r -= 1
            if (l > r or u > d):
                break
            for i in range(r, l - 1, - 1):
                res.append(matrix[d][i])
            d -= 1
            for i in range(d, u - 1, -1):
                res.append(matrix[i][l])
            l += 1
        return res