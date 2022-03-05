class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        
        i = 1
        if word[0].isupper():
            # 전부 대문자이거나, 맨 앞만 대문자여야 함
            if word[1].isupper():
                # 전부 대문자여야 함
                while i < len(word):
                    if word[i].islower():
                        return False
                    i += 1
                return True
            else:
                # 전부 소문자여야 함
                while i < len(word):
                    if word[i].isupper():
                        return False
                    i += 1
                return True
        else:
            # 전부 소문자여야 함
            while i < len(word):
                if word[i].isupper():
                    return False
                i += 1
            return True
