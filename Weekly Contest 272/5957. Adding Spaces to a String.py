class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # str_list = list(s)
        # for i in range(len(spaces)):
        #     str_list.insert(spaces[i]+i, ' ')
        # return ''.join(str_list)
        
        # for i, position in enumerate(spaces):
        #     str_list.insert(position + i, ' ')
        # return ''.join(str_list)
        
        # for i in spaces:
        #     s.replace(s[i], " "+s[i])[i-1: i]
        #     print(s)
        # return s
        
        # loop = 0
        # for i in spaces:
        #     s = s[0: i+loop] + ' ' + s[i+loop:]
        #     loop += 1
        # return s
        
        parts = [s[i:j] for i,j in zip([0]+spaces, spaces[0:]+[None])]
        return ' '.join(parts)
    
#         ans = []
#         for i in reversed(range(len(s))): 
#             ans.append(s[i])
#             if spaces and spaces[-1] == i: 
#                 ans.append(' ')
#                 spaces.pop()
#         return "".join(reversed(ans))
                
