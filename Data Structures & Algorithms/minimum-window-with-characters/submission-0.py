class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount, sCount = {}, {}

        for i in range(len(t)):
            tCount[t[i]] = 1 + tCount.get(t[i], 0)

        have = 0
        need = len(tCount)
        res = [-1, -1]
        resLen = float("infinity")
        
        l = 0
        for r in range(len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)

            if s[r] in tCount and sCount[s[r]] == tCount[s[r]]:
                have += 1

            while need == have:
                if (r-l+1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]

                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        if resLen != float("infinity"):
            return s[l:r+1]
        else:
            return ""
                

        