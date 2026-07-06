class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = dict()
        t_hash = dict()

        for i in range(len(s)):
            if s[i] in s_hash:
                s_hash[s[i]] += 1
            else:
                s_hash[s[i]] = 1

        for j in range(len(t)):
            if t[j] in t_hash:
                t_hash[t[j]] += 1
            else:
                t_hash[t[j]] = 1
        
        if t_hash == s_hash:
            return True
        else:
            return False