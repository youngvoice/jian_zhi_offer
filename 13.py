class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 深度优先遍历计数
        # 广度优先遍历计数
        def bitSum(integer):
            bit_sum = 0
            while True:
                bit_num = integer % 10
                bit_sum += bit_num
                integer = integer // 10
                if integer == 0:
                    return bit_sum
        length = max(m, n)
        bit_sum = [bitSum(i) for i in range(length)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        neighbors = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        def recursive(i, j):
            count = 0
            if 0 <= i < m and 0 <= j < n and bit_sum(i) + bit_sum(j) <= k and visited[i][j] == False:
                count += 1
                visited[i][j] = True
                for neighbor in neighbors:
                    count = count + recursive(i+neighbor[0], j+neighbor[1])
                
            return count
        return recursive(0,0)


            
        


        