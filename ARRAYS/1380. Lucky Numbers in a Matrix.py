#https://leetcode.com/problems/lucky-numbers-in-a-matrix/
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        min_in_row = [min(row) for row in matrix]
        max_in_col = []
        for j in range(n):
            col = []
            for i in range(m):
                col.append(matrix[i][j])
            max_in_col.append(max(col))
        return set(min_in_row).intersection(set(max_in_col))
