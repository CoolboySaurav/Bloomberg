class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        charMap = Counter(s)
        has_odd = 0
        count = 0
        
        if len(charMap) == 1:
            return len(s)
        
        for c, f in charMap.items():
            if f % 2:
                has_odd += 1
                count += f - 1
            else:
                count += f
        return count + 1 if has_odd else count