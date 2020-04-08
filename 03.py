# 217 219 220
# 287

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num not in visited:
                visited.add(num)
            else:
                return num

