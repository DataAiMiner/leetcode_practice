class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        range_list = s.split(':')
        c = [ord(s[0]) for s in range_list]
        r = [int(s[1]) for s in range_list]
        result, col = [], c[0]
        
        while col <= c[-1]:
            row = r[0]
            while row <= r[-1]:
                result.append(chr(col)+str(row))
                row += 1
            col += 1
                
        return result
        
