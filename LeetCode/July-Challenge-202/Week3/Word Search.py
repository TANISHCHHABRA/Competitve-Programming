class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        p=len(word)
        visited=set()
        def dfs(i,j,k):
            if board[i][j]==word[k]:
                if k==p-1:
                    return True
                visited.add((i,j))
                if i<m-1 and (i+1,j) not in visited:
                    right=dfs(i+1,j,k+1)
                else:
                    right = False
                if i>0 and (i-1,j) not in visited:
                    left = dfs(i-1,j,k+1)
                else:
                    left=False
                if j<n-1 and (i,j+1) not in visited:
                    down = dfs(i,j+1,k+1)
                else:
                    down = False
                if j>0 and (i,j-1) not in visited:
                    up = dfs(i,j-1,k+1)
                else:
                    up = False
                if not (left or right or up or down):
                    visited.remove((i,j))
                    return False
                else:
                    return True
            return False
    
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True
        return False
            
