#Returns the 0th indexed row of Pascal Triangle
class Solution:
    def getRow(self, rowIndex):
        row = []
        for i in range(rowIndex + 1):
            row.insert(0,1)
            for j in range(1, len(row)-1):
                row[j] = row[j] + row[j+1]
        return row
