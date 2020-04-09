class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        four_neighbors = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        visited = [[False for e in row] for row in board]
        m = len(board)
        n = len(board[0])

        # when k != len(word) -1 call this function
        def recursive(i, j, k, visited):# visited
            print("nei start ", i, " ", j)
            for neighbor in four_neighbors:
                i, j = i + neighbor[0], j + neighbor[1]
                k = k + 1
                print("nei ", i, " ", j)
                if  0 <= i < m and 0 <= j < n and visited[i][j] == False:
                    visited[i][j] = True
                    if board[i][j] == word[k]:
                        if k+1 == len(word):
                            print(i, " ", j)
                            return True
                        
                        if recursive(i, j, k, visited):
                            return True
                        else:
                            visited[i][j] = False
                            i, j = i - neighbor[0], j - neighbor[1]
                            k = k - 1

                    else:
                        visited[i][j] = False
                        #return False
                        i, j = i - neighbor[0], j - neighbor[1]
                        k = k - 1
                else:
                    i, j = i - neighbor[0], j - neighbor[1]
                    k = k - 1
            print("nei end ", i, " ", j)
            return False


        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if 1 == len(word):
                        return True
                    print("start", i, " ", j)
                    if recursive(i, j, 0, visited):
                        return True
                    else:
                        visited[i][j] = False
                
        return False