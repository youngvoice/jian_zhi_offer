'''
class Solution:
    def fib(self, N: int) -> int:
        if N != 0 and N != 1:
            return self.fib(N - 1) + self.fib(N - 2)
        elif N == 0:
            return 0
        else:# N == 1:
            return 1
''' 
'''
class Solution:
    def fib(self, N: int) -> int:
        if N != 1 and N != 0:
            fns1, fns2 = 1, 0
            for _ in range(N-1):
                fn = fns1 + fns2
                fns2 = fns1
                fns1 = fn
            return fn % 1000000007

        elif N == 1:
            return 1
        # N == 0
        else:
            return 0
'''

class Solution:
    def fib(self, N: int) -> int:
        a = 0
        b = 1
        for _ in range(N):
            #a = b
            #b = a + b
            a, b = b, a + b
        return a % 1000000007
