class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      def is_out(i, j):
        return i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0])

      seen = set()
      def dfs(i, j):
        print(f"dfs({i}, {j})")
        if is_out(i, j) or grid[i][j] == 0 or (i, j) in seen:
          return 0
        else:
          seen.add((i, j))
          return 1 + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i - 1, j)

      max_area = 0
      for i in range(len(grid)):
        for j in range(len(grid[0])):
          if grid[i][j] == 1:
            max_area = max(max_area, dfs(i, j))
      return max_area