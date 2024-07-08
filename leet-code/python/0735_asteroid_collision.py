class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        r = []
        for a in asteroids:
            if a < 0:
                while r and r[-1] > 0 and r[-1] < abs(a):
                    pa = r.pop()
                if r and r[-1] == abs(a):
                    r.pop()
                    continue
                if r and r[-1] > abs(a):
                    continue
        
            r.append(a)

        return r