class Solution:
    def capitalizeTitle(self, title: str) -> str:        
        title_list = title.split()
        result = []
        for word in title_list:
            if len(word) > 2:
                result.append(word.title())
            else:
                result.append(word.lower())
        return ' '.join(result)
