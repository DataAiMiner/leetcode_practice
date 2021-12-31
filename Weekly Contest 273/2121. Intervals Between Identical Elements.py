class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        record = dict()
        
        for ind, num in enumerate(arr):
            indices = [i for i, x in enumerate(arr) if x == num and i != ind]
            record[ind] = indices
        
        for ind, indices in record:
            sum = 0
            for other in indices:
                sum += abs(ind-other)
            result[ind] = sum
        
        return result
