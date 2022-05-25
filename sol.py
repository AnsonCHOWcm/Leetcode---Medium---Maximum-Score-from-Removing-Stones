class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        target = max(a, b, c)

        if (a + b + c - 2 * target <= 0):
            return (a + b + c - target)

        return (target + (a + b + c - 2 * target) // 2)