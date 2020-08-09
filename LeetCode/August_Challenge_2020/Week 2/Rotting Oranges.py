class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #BFS - count fresh, each time one rots, decrement, return once 0
        if len(grid) <= 0 or len(grid[0]) <= 0:
            return -1
        
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        m, n = len(grid), len(grid[0])
        freshCount = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == FRESH:
                    freshCount +=1
                elif grid[i][j] == ROTTEN:
                    q.append((i, j, 0))
        
        if freshCount == 0:
            return 0
        
        neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
        while len(q) > 0:
            nxtI, nxtJ, nxtMin = q.popleft()
            for nei in neighbors:
                y = nxtI + nei[0] 
                x = nxtJ + nei[1]
                if y >=0 and y < m and x >= 0 and x < n:
                    if grid[y][x] not in {ROTTEN, EMPTY}:
                        grid[y][x] = ROTTEN
                        #print(nxtMin + 1, grid)
                        freshCount -=1
                        if freshCount == 0:
                            return nxtMin + 1
                        q.append((y, x, nxtMin + 1))
                        
        return -1
            
        
