## https://leetcode.com/problems/can-place-flowers/discuss/1698771/C%2B%2BJavaPython-2-Simple-Solutions-oror-Image-Explanation-oror-Beginner-Friendly
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0: return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):  # can place?
                n -= 1
                if n == 0: return True
                flowerbed[i] = 1  # palce!
        return False

## https://leetcode.com/problems/can-place-flowers/discuss/1048610/Python-Simple-solution-using-counti
# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         if not n:  # if n = 0
#             return True
        
#         flowerbed.append(0)
#         count, i, f = 0, 0, len(flowerbed)

#         while i < f-1:
#             if flowerbed[i]:  # if theres a flower, increment index by 2. Note we already know that the flowerbed[i+1] = 0
#                 i += 2
#             elif not flowerbed[i+1]:  # if no flowers, check if the next plot has flowers
#                 count += 1
#                 i += 2
#                 if count == n: return True
#             else: # if flower at flowerbed[i+1], we know theres no flowers at flowerbed[i+2], and next valid position is flowerbed[i+3]
#                 i += 3

#         return False
