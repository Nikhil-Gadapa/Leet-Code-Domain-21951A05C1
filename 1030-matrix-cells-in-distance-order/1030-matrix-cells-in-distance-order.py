class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        cells=[(i,j) for i in range(rows) for j in range(cols)]
        distance=sorted(cells,key= lambda cell: abs(cell[0]-rCenter)+abs(cell[1]-cCenter))
        return distance
        