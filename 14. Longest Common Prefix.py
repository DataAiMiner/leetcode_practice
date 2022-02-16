class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        min_len = min([len(str) for str in strs])
        for i in range(min_len):
            start = strs[0][i]
            for j in range(1, len(strs)):
                if start != strs[j][i]:
                    return result
                else:
                    start = strs[j][i]
            result += start
        
        return result
