# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        result = 0
        
        def visit(grid, i, j):
            visited[i][j] = True
            for step in steps:
                ni, nj = i + step[0], j + step[1]
                if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]):
                    continue
                if grid[ni][nj] == '1' and not visited[ni][nj]:
                    visit(grid, ni, nj)                    
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    # check
                    visit(grid, i, j)
                    result += 1
        
        return result
