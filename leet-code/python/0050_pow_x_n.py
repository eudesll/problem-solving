class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(base, exp):
            if exp == 0:
                return 1

            if exp % 2 == 0:
                return pow(base * base, exp // 2)
            
            return base * pow(base * base, (exp - 1) // 2)
        
        res = pow(x, abs(n))
        return float(res) if n >= 0 else 1/res