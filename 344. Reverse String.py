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


# ## One Liner (https://leetcode.com/problems/reverse-string/discuss/669571/Python-Oneliner-two-pointers-explained)
# class Solution:
#     def reverseString(self, s):
#         for i in range(len(s)//2): s[i], s[-i-1] = s[-i-1], s[i]
            
# ## Bitwise
# class Solution:
#     def reverseString(self, s):
#         for i in range(len(s)//2): s[i], s[~i] = s[~i], s[i]
