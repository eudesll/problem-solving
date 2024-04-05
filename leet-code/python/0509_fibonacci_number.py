class Solution:
  # calc = {0: 0, 1: 1}
  
  def fib(self, n: int) -> int:
    golden_ratio = (1+(5 ** 0.5))/2
    return int(round((golden_ratio ** n)/ 5 ** 0.5))
      
    # if n in self.calc:
    #   return self.calc[n]
    
    # self.calc[n] = self.fib(n - 1) + self.fib(n - 2)
    # return self.calc[n]
