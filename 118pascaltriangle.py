#Returns a given up to given row of pascal triangle
class Solution:
    def generate(self, numRows):
        triangle = []
        row = []
        for i in range(numRows):
            row.insert(0,1)
            for j in range(1, len(row)-1):
                row[j] = row[j] + row[j+1]
            triangle.append(row[:])
        return triangle

    list = generate(5)
    print(list)
