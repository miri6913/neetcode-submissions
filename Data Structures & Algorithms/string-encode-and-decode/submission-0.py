class Solution:

    def encode(self, strs: List[str]) -> str:
        en_res = ""

        for i in strs:
            en_res += str(len(i)) + "#" + i

        print(en_res)
        return en_res

    def decode(self, s: str) -> List[str]:
        dec_res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            str_len = int(s[i:j])
            dec_res.append(s[j+1:j+1+str_len])
            i = j + 1 + str_len
        return dec_res

