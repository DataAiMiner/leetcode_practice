class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == "" and needle != "":
            return -1
        if needle == haystack or needle == "":
            return 0
        
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
