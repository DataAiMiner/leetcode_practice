class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        record = set()
        while n != 1:
            n = sum([int(num)**2 for num in str(n)])
            if n in record:
                return False
            record.add(n)
        
        return True
        
#         n_list = [num for num in str(n)]
#         init_n = 0
        
#         while (n <= (2**31 -1) and n>= 1) and (init_n != n):
#             n_list_sum = sum([int(num)**2 for num in n_list])
#             if n_list_sum == 1:
#                 return True
#             else:
#                 n_list = [num for num in str(n_list_sum)]
#                 n = n_list_sum
        
#         return False
