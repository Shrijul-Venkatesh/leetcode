class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        zeros = 0
        max_len = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            # If more than 1 zero, shrink window from the left
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            # Current window length is right - left + 1,
            # but we must delete exactly one element
            max_len = max(max_len, right - left + 1 - 1)
        
        return max_len
