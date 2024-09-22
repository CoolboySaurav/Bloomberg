class Solution(object):
    
    def solve(self, num):
        sum = 0
        while num > 0:
            sum += ((num % 10) ** 2)
            num //= 10
        return sum
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        slow = fast = n
        
        while True:
            slow = self.solve(slow)
            fast = self.solve(self.solve(fast))
            if slow == fast:
                if slow == fast == 1:
                    return True
                else:
                    return False
    