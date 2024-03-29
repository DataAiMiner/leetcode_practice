class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            if i % 3 == 0:
                if i % 5 == 0:
                    result.append("FizzBuzz")
                else:
                    result.append("Fizz")
            else:
                if i % 5 == 0:
                    result.append("Buzz")
                else:
                    result.append(str(i))
        
        return result

## more concise solution
#     def fizzBuzz(self, n):
#         return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
