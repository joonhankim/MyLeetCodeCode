class Solution:
    def modifyString(self, s: str) -> str:
        if s == '?':
            return 'a'
        
        s_set = set(s)
        available_chars = set()
        
        for char in s:
            if char == '?':
                if not available_chars:
                    available_chars = set('abcdefghijklmnopqrstuvwxyz').difference(s_set)
                s = s.replace(char, available_chars.pop(), 1)
        return s