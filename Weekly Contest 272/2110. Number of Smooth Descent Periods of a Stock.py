class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 1
        
        n = len(prices)
        result, current = 0, 1

        for i in range(1, n):
            if prices[i] == prices[i - 1] - 1:
                current += 1
            else:
                result += current * (current + 1) // 2
                current = 1
        return result + current * (current + 1) // 2
