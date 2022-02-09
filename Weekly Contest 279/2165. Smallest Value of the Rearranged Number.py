class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0 :
            return num
        
        if num < 0:
            # 큰 것부터 나열
            num_str = sorted(list(str(num * (-1))), reverse=True)
        else:
            # 작은 것부터 나열
            num_str = sorted(list(str(num)))
        
        # 0 개수 세기
        num_zeros = collections.Counter(num_str)['0']
        result = ""
        
        if num < 0:
            result = ''.join(num_str)
            return int(result)*(-1)
        else:
            result = ''.join([num_str[num_zeros]] + num_str[:num_zeros] + num_str[num_zeros+1:])
            return int(result) 
