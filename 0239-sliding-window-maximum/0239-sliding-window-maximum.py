class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        st = deque()
        l = r = 0
        
        while r < len(nums):
            while st and nums[st[-1]] < nums[r]:
                st.pop()
            st.append(r)
            
            if st[0] < l:
                st.popleft()

            
            if r + 1 >= k  :
                res.append(nums[st[0]])
                l += 1
            r += 1
        return res