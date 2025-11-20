class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        
        freq = defaultdict(int)
        operations = 0
        
        for num in nums:
            complement = k - num
            # If we have a complement available, form a pair
            if freq[complement] > 0:
                freq[complement] -= 1
                operations += 1
            else:
                # Otherwise, store this number for future pairing
                freq[num] += 1
        
        return operations
