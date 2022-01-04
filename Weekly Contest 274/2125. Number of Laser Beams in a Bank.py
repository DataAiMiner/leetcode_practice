class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
      # 각 행마다 있는 security device 수를 계속 곱해서 더해 나간다
        bank_2d = [list(line) for line in bank]
        result = 0
        saved = 0
        for row in bank_2d: 
            count = row.count('1')
#             print(count)
            if count != 0: 
                result += saved * count
                saved = count 
        return result
