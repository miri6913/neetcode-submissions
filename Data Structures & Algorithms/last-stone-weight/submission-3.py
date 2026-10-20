class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        print(stones)
        heapq.heapify(stones)
        print(stones)

        while len(stones) > 1:
            tmp1, tmp2 = -heapq.heappop(stones), -heapq.heappop(stones)
            print(stones)
            if tmp1 == tmp2:
                continue
            if tmp1 > tmp2:
                heapq.heappush(stones, -(tmp1 - tmp2))
        
        return abs(stones[0]) if stones else 0