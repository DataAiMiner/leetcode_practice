class Solution:
    def isValid(self, s):
        map = {')':'(', '}':'{', ']':'['}
        st = []
        for e in s:
            print(e)
            if st and (e in map and st[-1] == map[e]):
                print(st.pop())
            else:
                st.append(e)
                print('else' + str(st))
        return not st
