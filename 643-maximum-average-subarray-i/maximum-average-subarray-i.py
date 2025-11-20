class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Sum of the first window
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Slide the window over the array
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum
        
        return float(max_sum) / k
