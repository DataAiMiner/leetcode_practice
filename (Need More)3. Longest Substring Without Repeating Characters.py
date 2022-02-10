class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
               max_length = max(max_length, i - start + 1)
            used[c] = i
        return max_length

#         counter = collections.Counter(s)
#         uniques = []
        
#         longest_str = []
#         max_num = 0
        
#         for char in s:
#             if char not in longest_str:
#                 longest_str.append(char)
#             else:
#                 max_num = max(max_num, len(longest_str))
#                 longest_str.remove(char)
#                 longest_str.append(char)
        
#         return max(max_num, len(longest_str))
