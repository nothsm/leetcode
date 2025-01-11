class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        seen = set()
        def dfs(i, j):
            if 0 <= i and i < len(grid) and 0 <= j and j < len(grid[0]) and (i, j) not in seen and grid[i][j] == 1:
                seen.add((i, j))
                return 1 + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1)
            else:
                return 0

        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = max(dfs(i, j), area)
        return area