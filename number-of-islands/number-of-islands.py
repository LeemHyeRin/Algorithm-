class Solution(object):
    def numIslands(self, grid) :   
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1,j)
            dfs(i-1,j)
            
        
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
        
        return count