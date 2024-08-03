class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #find out the number of rows and columns in the grid
        all_rows = len(grid)
        all_cols = len(grid[0])

        #initialize number of islands to 0
        num_islands = 0


        #DFS function to find out whether the island is connected
        def dfs(row, col):

            #Base Case: Checks whether index is out of bounds or grid[row][col] != 1
            if row >= all_rows or col >= all_cols or row < 0 or col < 0 or grid[row][col] != "1":
                return
            else:
                #convert grid[row][col] to water
                grid[row][col] = "0"
                dfs(row, col+1)
                dfs(row+1, col)
                dfs(row, col-1)
                dfs(row-1, col)

        # loop through the grid
        for row in range(all_rows):
            for col in range(all_cols):
                if grid[row][col] == "1":
                    num_islands += 1
                    dfs(row, col)

        return num_islands

        #Time Complexity = O(mxn)
        #Space Complexity = O(mxn)
        