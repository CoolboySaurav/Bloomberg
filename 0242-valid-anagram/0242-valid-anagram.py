class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s or not t or len(s) != len(t):
            return False
        charMap = [0] * 26
        
        for i in range(len(s)):
            index1 = ord(s[i]) - ord('a')
            index2 = ord(t[i]) - ord('a')
            charMap[index1] += 1
            charMap[index2] -= 1
        
        for i in charMap:
            if i != 0:
                return False
        return True