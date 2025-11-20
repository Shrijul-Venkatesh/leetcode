class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        from collections import Counter
        
        freq = Counter(arr)              # value → occurrences
        counts = freq.values()           # list of occurrence counts
        
        return len(counts) == len(set(counts))
