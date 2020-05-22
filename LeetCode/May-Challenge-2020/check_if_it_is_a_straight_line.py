class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if(len(coordinates) == 2):
            return True
        first = coordinates[0]
        second = coordinates[1]
        if((second[0] - first[0]) == 0):
            m = 0
        else:
            m = (second[1] - first[1]) / (second[0] - first[0])
        y = second[1]
        x = second[0]
        c = y - (m*x)
        #y = m*x + c
        for i in range(2,len(coordinates)):
            x = coordinates[i][0]
            y = coordinates[i][1]
            if(y == (m*x + c)):
                continue
            else:
                return False
        return True
