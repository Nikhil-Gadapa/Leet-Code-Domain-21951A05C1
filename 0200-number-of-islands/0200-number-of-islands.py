from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    stack = [(r, c)]
                    while stack:
                        x, y = stack.pop()
                        if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "1":
                            grid[x][y] = "0"
                            stack.append((x + 1, y))
                            stack.append((x - 1, y))
                            stack.append((x, y + 1))
                            stack.append((x, y - 1))
                    num_islands += 1
        
        return num_islands

