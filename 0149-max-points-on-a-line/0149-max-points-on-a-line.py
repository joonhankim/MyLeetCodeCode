from math import gcd
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points)
        def get_gradient(list_a, list_b):
            dx, dy = list_a[0] - list_b[0], list_a[1] - list_b[1]
            if dx == 0:
                return "infinity"
            g = gcd(dx, dy)
            return (dy // g, dx // g)
        if len(points) <= 2:
            return len(points)
        max_same_gradients = 1
        for i in range(len(sorted_points)):
            slopes = defaultdict(int)
            standard = 1
            for j in range(len(sorted_points)):
                if i != j:
                    slopes[get_gradient(sorted_points[i], sorted_points[j])] += 1
            max_same_gradients = max(max_same_gradients, max(slopes.values(), default=0) + standard)
        return max_same_gradients