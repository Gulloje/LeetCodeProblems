#Returns a given row of pascal triangle
class solution:
    def generateRows(numRows):
        triangle = []
        row = []
        for i in range(numRows):
            row.insert(0,1)
            for j in range(1, len(row)-1):
                row[j] = row[j] + row[j+1]
            triangle.append(row[:])
        return triangle

    list = generateRows(5)
    print(list)