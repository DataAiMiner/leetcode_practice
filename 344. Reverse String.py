class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = len(s) // 2
        ind = 0
        if len(s) % 2 == 1:
            while (start + ind) <= len(s)-1:
                s[start + ind], s[start - ind]  = s[start - ind], s[start + ind]
                ind += 1
        else:
            while (start + ind) <= len(s)-1:
                s[start + ind], s[start - ind -1]  = s[start - ind -1], s[start + ind]
                ind += 1
        
