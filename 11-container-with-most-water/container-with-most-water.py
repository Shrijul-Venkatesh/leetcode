class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Current width between the two lines
            width = right - left
            
            # Height of the container is limited by the shorter line
            h = min(height[left], height[right])
            
            # Calculate area
            max_area = max(max_area, h * width)
            
            # Move the pointer at the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
