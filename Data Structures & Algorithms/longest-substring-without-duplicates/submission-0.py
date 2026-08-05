class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp_set = set()
        l, res = 0, 0
        
        for r in range(len(s)):
            while s[r] in tmp_set:
                tmp_set.remove(s[l])
                l += 1
            tmp_set.add(s[r])
            res = max(res, r-l+1)

        return res
        