class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        # 1. make list of maxLen
        maxLenList = []
        for rect in rectangles:
            longer = rect[0]
            for len in rect:
                if len <= longer:
                    longer = len
            maxLenList.append(longer)
        
        # 2. find out largest one
        max = 0
        for len in maxLenList:
            if len >= max:
                max = len
        
        # 3. count matching ones
        count = 0
        for len in maxLenList:
            if len == max:
                count += 1
        
        return count
