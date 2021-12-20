class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 1
        
        n = len(prices)
        result, current = 0, 1

        # 소그룹으로 묶을 수 있는 것들(if)와 개별로 노는 것(else)로 나눌 수 있다.
        # 소그룹을 이루는 원소의 수가 N이면, 해당 소그룹에서 나올 수 있는 모든 경우의 수는 N(N+1)/2 가지
        for i in range(1, n):
            if prices[i] == prices[i - 1] - 1:
                current += 1
            else:
                result += current * (current + 1) // 2
                current = 1
        return result + current * (current + 1) // 2
