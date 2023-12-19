class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        seen=[]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                seen.append(matrix[i][j])
        seen.sort()
        return seen[k-1]
            