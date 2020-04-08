'''
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        def recursive(left, right):
            #if numbers[left] < numbers[right]:
            #    return numbers[left]
            #elif left + 1 == right:
            if left + 1 == right:
                return numbers[right]
            else:
                print('a',left, right)
                mid = (left + right) // 2
                if numbers[mid] > numbers[left]:
                    left = mid
                elif numbers[mid] < numbers[right]:
                    right = mid
                else:
                    pass
                print('b',left, right)
                return recursive(left, right)

        length = len(numbers)
        if numbers[0] < numbers[length - 1]:
            return numbers[0]
        return recursive(0, length - 1)
            
'''

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        def recursive(left, right):
            #if numbers[left] < numbers[right]:
            #    return numbers[left]
            #elif left + 1 == right:
            if left + 1 == right:
                return numbers[right]
            else:
                #print('a',left, right)
                mid = (left + right) // 2
                if numbers[mid] > numbers[left]:
                    left = mid
                elif numbers[mid] < numbers[right]:
                    right = mid
                else:
                    ret = numbers[left]
                    i = left
                    while i <= right:
                        if ret > numbers[i]:
                            ret = numbers[i]
                        i += 1
                    return ret
                #print('b',left, right)
                return recursive(left, right)

        length = len(numbers)
        if numbers[0] < numbers[length - 1]:
            return numbers[0]
        return recursive(0, length - 1)
            


