class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        ans = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans += 4
                    
                    if  i > 0 and grid[i-1][j] == 1:
                        ans -= 2
                        
                    if j > 0 and grid[i][j-1] == 1:
                        ans -= 2
        
        return ans
