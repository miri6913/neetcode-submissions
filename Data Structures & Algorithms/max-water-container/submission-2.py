class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left, right = 0, len(heights)-1

        for i in range(len(heights)):
            for j in range(len(heights)-1, i, -1):
                tmp_area = min(heights[i], heights[j]) * (j-i)
                if tmp_area > max_area:
                    max_area = tmp_area
        
        return max_area
        