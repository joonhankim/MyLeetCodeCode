class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        all_combinations = []

        def generate_combinations(combination: str, index: int):

            if index == len(s):
                all_combinations.append(combination)
                return

            if s[index].isalpha():

                generate_combinations(combination + s[index].lower(), index + 1)
                generate_combinations(combination + s[index].upper(), index + 1)
            else:
                generate_combinations(combination + s[index], index + 1)
        
        generate_combinations("", 0)
        return all_combinations