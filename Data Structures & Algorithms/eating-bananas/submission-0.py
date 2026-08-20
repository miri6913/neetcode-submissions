import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = left

        while left <= right:
            mid = (left + right) // 2

            tmpTime = 0
            for i in piles:
                tmpTime += math.ceil(i/mid)
            
            if tmpTime <= h:
                right = mid - 1
                result = mid
            elif tmpTime > h:
                left = mid + 1

        return result
        
        