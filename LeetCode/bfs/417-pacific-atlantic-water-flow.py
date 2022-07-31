class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        steps = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m, n = len(heights[0]), len(heights)
        p_visited = [[False for _ in range(m)] for _ in range(n)]
        a_visited = [[False for _ in range(m)] for _ in range(n)]

        p_border = []
        a_border = []
        
        result = []
        def bfs(border, visited, cell):
            
            i, j = cell[0], cell[1]
            for step in steps:
                ni, nj = i + step[0], j + step[1]
                if ni < 0 or ni >= n or nj < 0 or nj >= m or\
                   visited[ni][nj] or\
                   heights[ni][nj] < heights[i][j]:
                    continue
                visited[ni][nj] = True
                bfs(border, visited, (ni, nj))        
        
        # horizontal border setup
        for i in range(m):
            p_border.append((0, i))
            a_border.append((n - 1, i))
            
            p_visited[0][i] = True
            a_visited[n - 1][i] = True
        
        # vertical border setup
        for i in range(n):
            p_border.append((i, 0))
            a_border.append((i, m - 1))
            
            p_visited[i][0] = True
            a_visited[i][m - 1] = True

        for cell in p_border:
            bfs(p_border, p_visited, cell)

        for cell in a_border:
            bfs(a_border, a_visited, cell)
            
        for i in range(n):
            for j in range(m):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i, j])
        
        return result
