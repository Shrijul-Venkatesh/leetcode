class Solution:
    def increasingTriplet(self, nums):
        n = len(nums)
        if n < 3:
            return False

        prefix_min = [0]*n
        prefix_min[0] = nums[0]
        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i-1], nums[i])

        suffix_max = [0]*n
        suffix_max[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], nums[i])

        # check for some middle index j
        for j in range(1, n-1):
            if prefix_min[j-1] < nums[j] < suffix_max[j+1]:
                return True
        return False
