class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sample_result = []
        tmp_dic = {}

        for i in range(len(nums)):
            tmp_dic[nums[i]] = 1 + tmp_dic.get(nums[i], 0)

        sorted_dic = sorted(tmp_dic.values(), reverse=True)

        for i in range(k):
            for j in tmp_dic:
                if sorted_dic[i] == tmp_dic[j]:
                    sample_result.append(j)

        sample_result = list(set(sample_result))
        return sample_result