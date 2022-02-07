class Solution:
    def minimumSum(self, num: int) -> int:
        num_str = sorted(list(str(num)), reverse=True)
        
        num1 = str(num_str.pop())
        num2 = str(num_str.pop())
        num1 += str(num_str.pop())
        num2 += str(num_str.pop())
        
        return int(num1)+int(num2)

## More classy
# class Solution:
#     def minimumSum(self, num: int) -> int:
#         a = sorted(str(num))
#         return int(a[0] + a[2]) + int(a[1] + a[3])
