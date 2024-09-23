class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def solve(p):
            tot = 0
            count = 0
            
            for i in bloomDay:
                if i <= p:
                    count += 1
                else:
                    tot += count // k
                    count = 0
            tot += count // k
            return tot >= m
        
        if (m * k) > len(bloomDay):
            return -1
        
        l, r = 1, max(bloomDay)
        ans = r
        
        while l <= r:
            mid = l + (r - l) // 2
            if solve(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return ans