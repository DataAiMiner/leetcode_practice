class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i, word in enumerate(words):
            chars = list(word)
            
            low, high = 0, len(chars)-1
            if len(chars) % 2 == 0:
                while low < high:
                    if chars[low] != chars[high]:
                        break
                    else:
                        low, high = low+1, high-1
                if chars[low] == chars[high] and high == low-1:
                    return word
            else:
                mid = (low + high) // 2
                while low != high:
                    if chars[low] != chars[high]:
                        break
                    else:
                        low, high = low+1, high-1
                if low == mid and high == mid:
                    return word
       
        return ""
