class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)

        for i in strs:
            sorted_st = ''.join(sorted(i))

            ana[sorted_st].append(i)

        return list(ana.values())
        
        
        