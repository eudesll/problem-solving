class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = []
        res = 0
        for n in nums:
            while s and s[-1] > n:
                s.pop()

            if n == 0:
                continue

            if not s or s[-1] < n:
                res += 1
                s.append(n)

        return res