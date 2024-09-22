class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def helper(open, close, path):
            if (len(path) == 2*n) and (open == close == n):
                res.append(path)
                return
            if open < n:
                helper(open + 1, close, path + "(")
            if open > close:
                helper(open, close + 1, path + ")")
        helper(0,0,"")
        return res