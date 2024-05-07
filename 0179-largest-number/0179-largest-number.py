class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums_str = list(map(str, nums))
        
        nums_str.sort(key=lambda x: x*9, reverse=True)
        
        if all(x == '0' for x in nums_str):
            return "0"

        return ''.join(nums_str)