class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tmp = {}

        for i in range(len(nums)):
            tmp[nums[i]] = 1 + tmp.get(nums[i], 0)
            if(tmp[nums[i]] >= 2):
                return nums[i]
        
        print(tmp)
        