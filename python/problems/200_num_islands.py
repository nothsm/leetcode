class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      seen = set()
      def dfs(i, j):
        if (i, j) not in seen and (0 <= i and i < len(grid)) and (0 <= j and j < len(grid[0])) and grid[i][j] == "1":
          seen.add((i, j))
          dfs(i + 1, j)
          dfs(i - 1, j)
          dfs(i, j + 1)
          dfs(i, j - 1)

      islands = 0
      for i in range(len(grid)):
        for j in range(len(grid[0])):
          if grid[i][j] == "1" and (i, j) not in seen:
            islands += 1
            dfs(i, j)
      return islands
        