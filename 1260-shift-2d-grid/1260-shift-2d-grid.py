class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        total_elements = m * n
        
        # Optimize k if it is larger than the total number of elements
        k = k % total_elements
        
        # Flatten the 2D grid into a 1D list
        flat_grid = []
        for row in grid:
            flat_grid.extend(row)
            
        # Perform the shift operation using slicing
        # Elements from the back move to the front, and front moves to the back
        shifted_flat = flat_grid[-k:] + flat_grid[:-k]
        
        # Reconstruct the 1D list back into an m x n 2D grid
        result = []
        for i in range(0, total_elements, n):
            result.append(shifted_flat[i : i + n])
            
        return result
