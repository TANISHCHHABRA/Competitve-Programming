class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        N %= 14
        if not N:
            N = 14
        temp = cells.copy()
        for j in range(1,7):
            if cells[j-1]==0 and cells[j+1]==0:
                temp[j] = 1
            elif cells[j-1]==1 and cells[j+1]==1:
                temp[j] = 1
            else:
                temp[j] = 0
        cells = temp
        
        cells[0] = 0
        cells[-1] = 0
        
        for i in range(N-1):
            temp = cells.copy()
            for j in range(1,7):
                if cells[j-1]==0 and cells[j+1]==0:
                    temp[j] = 1
                elif cells[j-1]==1 and cells[j+1]==1:
                    temp[j] = 1
                else:
                    temp[j] = 0
            cells = temp
        return cells
                
