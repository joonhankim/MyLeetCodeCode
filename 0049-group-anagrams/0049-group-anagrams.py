class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        def check_anagram(word):
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
            return None
        
        for word in strs:
            check_anagram(word)

        final_ans = list(anagrams.values())
        
        return final_ans
        
        
        