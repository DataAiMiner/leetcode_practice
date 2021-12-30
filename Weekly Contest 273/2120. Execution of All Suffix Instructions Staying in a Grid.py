class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        if n == 1:
            return [0]*len(s)
        
        result = []
        
        for i in range(len(s)):
            print(s[i:])
            x_pos, y_pos = startPos[0], startPos[1]
            count = 0
            for direction in s[i:]:
                if direction == 'L':
                    y_pos -= 1
                elif direction == 'R':
                    y_pos += 1
                elif direction == 'U':
                    x_pos -= 1
                elif direction == 'D':
                    x_pos += 1
                    
                if x_pos<0 or x_pos>=n or y_pos<0 or y_pos>=n:
                    break
                else:
                    count += 1
            result.append(count)
        
        return result
