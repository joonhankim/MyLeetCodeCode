class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        hashmap = defaultdict(list)
        for n in arr:
            digit_sum = 0
            num = n
            while num:
                digit_sum += num % 10
                num //= 10
            hashmap[digit_sum].append(n)

        ans = -1
        for v in hashmap.values():
            if len(v) > 1:
                v = sorted(v,reverse=True)
                ans = max(ans, v[0] + v[1])
        return ans 
                
                
                
        