# f(n) = f(n-1) + f(n - 2)
class Solution:
    def numWays(self, n: int) -> int:
        f0 = 1
        f1 = 1
        fn_1 = f1
        fn_2 = f0
        if n < 2:
            fn = 1
        else:
            fn = 0
        for i in range(2, n+1):
            fn = fn_1 + fn_2
            fn_2 = fn_1
            fn_1 = fn
        return fn % 1000000007
            