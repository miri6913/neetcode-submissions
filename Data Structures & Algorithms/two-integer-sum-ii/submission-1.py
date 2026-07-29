class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if ((numbers[i]+numbers[j]) == target) and (numbers[i]<numbers[j]):
                    print(numbers[i], numbers[j])
                    res.extend([i+1, j+1])

        return res
        