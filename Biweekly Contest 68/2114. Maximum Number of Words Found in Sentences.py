class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        N = 0
        for sentence in sentences:
            n = len(sentence.split(" "))
            N = max(n, N)
        return N
