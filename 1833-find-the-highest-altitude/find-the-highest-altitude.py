class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = 0
        max_altitude = 0   # starts at 0 because point 0 has altitude 0
        
        for g in gain:
            altitude += g
            if altitude > max_altitude:
                max_altitude = altitude
        
        return max_altitude
