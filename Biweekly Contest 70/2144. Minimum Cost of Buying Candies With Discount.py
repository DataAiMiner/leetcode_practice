class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        payment, i, N = 0, 0, len(cost)
        
        while i < N:
            payment += sum(cost[i : i + 2])
            i += 3
        
        return payment
