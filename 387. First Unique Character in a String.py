class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        unique_ones = [pair for pair in counter if counter[pair] == 1]
        
        ind = len(s)
        if len(unique_ones) == 0:
            ind = -1
        else:
            for i in range(len(unique_ones)):
                ind = min(s.index(unique_ones[i]), ind)
        
        return ind
