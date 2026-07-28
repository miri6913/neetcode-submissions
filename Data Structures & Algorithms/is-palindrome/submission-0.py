class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s[::-1])
        res = ''
        for i in s:
            if i.isalnum():
                res += i.lower()
        
        return res == res[::-1]