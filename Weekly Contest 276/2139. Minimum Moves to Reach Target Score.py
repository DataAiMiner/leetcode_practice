class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        init, count = 1, 0
        
        if maxDoubles == 0:
            return target-1

        while target > 1 and maxDoubles > 0:
            leftover = target % 2
            if leftover == 0:
                target /= 2
                count += 1
                maxDoubles -= 1
            elif leftover == 1:
                target -= 1
                count += 1
        
        if target != init:
            count += (target-init)
        
        return int(count)
