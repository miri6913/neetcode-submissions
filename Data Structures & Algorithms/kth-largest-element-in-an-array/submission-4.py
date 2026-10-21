class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        tmp = [-num for num in nums]
        heapq.heapify(tmp)

        while k > 1:
            heapq.heappop(tmp)
            k -= 1

        return -tmp[0] if tmp else 0    


        