class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        print(f"set_nums: {set_nums}")
        longest = 0

        for i in set_nums:
            
            if (i-1) not in set_nums:
                length = 1    
                
                while (i+length) in set_nums:
                    length += 1
                longest = max(length, longest)

        
        return(longest)
                    

        