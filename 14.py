'''
class Solution:
    def cuttingRope(self, n: int) -> int:
        product = [0,1]
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        product.append(1)
        product.append(2)
        for j in range(4, n+1):
            max = j-1 
            for i in range(2, j//2 + 1):
                p = product[i]*product[j-i]
                if p > max:
                    max = p
            product.append(max)
        return product[n]
'''
'''
class Solution:
    def cuttingRope(self, n: int) -> int:
        product = [0,1]
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        product.append(1)
        product.append(2)
        for j in range(4, n+1):
            #max = j-1 
            #for i in range(2, j//2 + 1):
            max = 0
            for i in range(1, j//2 + 1):
                p_no = i*(j-i)
                if p_no > max:
                    max = p_no
                
                if i > 1:
                    
                    p_yes = product[i]*product[j-i]
                    if j == 8:
                        print(i, ' ',j - i, ' ',max, ' ', p_yes)
                    if p_yes > max:
                        max = p_yes
            product.append(max)
        return product[n]
'''

'''
class Solution:
    def cuttingRope(self, n: int) -> int:
        product = [1,1]
        if n == 2:
            return 1
        else: # n > 2
            product.append(2)
        for i in range(3, n):
            max = 0
            #for j in (1, i//2 + 1):
            product.append(i)
            for j in range(0, i//2 + 1):
                mul = product[j]*product[i - j]
                if mul > max:
                    max = mul
            #product.append(max)
            product[i] = max
        #if n == 3:
        #    return 2
        ################
        # product[n-1]
        max = 0
        for j in range(1, n//2 + 1):
            mul = product[j]*product[n - j]
            #print(j, ' ', mul)
            if mul > max:
                max = mul
        return max

'''

class Solution:
    def cuttingRope(self, n: int) -> int:
        product = [0, 1, 2, 3, 4]
        if n < 5:
            if n == 2:
                return 1
            elif n == 3:
                return 2
            else:
                return 4
        else:
            sum = 1
            while n >= 5:
                sum = 3*sum
                n = n - 3
                
            sum = sum*product[n]
        return sum

