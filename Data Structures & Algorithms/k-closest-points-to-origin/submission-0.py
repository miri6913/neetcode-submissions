class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tmp = []
        for x, y in points:
            dist = math.sqrt((0-x)**2 + (0-y)**2)
            tmp.append([dist, x, y])

        heapq.heapify(tmp)

        res = []

        while k > 0:
            dist, x, y = heapq.heappop(tmp)
            res.append([x, y])
            k -= 1

        return res