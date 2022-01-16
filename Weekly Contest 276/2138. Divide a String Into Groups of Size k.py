class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        start, cut = 0, k
        result = []
        
        total_len = len(s)     
        
        while cut <= (total_len + k):
            result.append(s[start:cut])
            start, cut = cut, cut+k
            
        if (total_len%k) != 0:
            prep = fill * (k - (total_len%k))
            result[-1] = result[-1]+prep
        else:
            result.pop()
        
        return result
