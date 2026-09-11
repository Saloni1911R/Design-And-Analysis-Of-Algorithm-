from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        m = len(classroom)
        n = len(classroom[0])
        
        start_r, start_c = -1, -1
        litter_map = {}
        litter_count = 0
        
        # Identify start and assign index flags to each litter
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_map[(r, c)] = litter_count
                    litter_count += 1
                    
        target_mask = (1 << litter_count) - 1
        
        # 3D visited structure: visited[r][c][mask] = max_remaining_energy_seen
        # Initialized to -1 (unvisited/invalid)
        visited = [[[-1] * (1 << litter_count) for _ in range(n)] for _ in range(m)]
        
        initial_mask = 0
        if (start_r, start_c) in litter_map:
            initial_mask |= (1 << litter_map[(start_r, start_c)])
            
        queue = deque([(start_r, start_c, energy, initial_mask, 0)])
        visited[start_r][start_c][initial_mask] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, curr_energy, mask, moves = queue.popleft()
            
            # Goal check: all litter collected
            if mask == target_mask:
                return moves
                
            # If we've already found a way to reach this cell/mask with strictly 
            # more energy, skip processing this path.
            if visited[r][c][mask] > curr_energy:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds and obstacles
                if not (0 <= nr < m and 0 <= nc < n) or classroom[nr][nc] == 'X':
                    continue
                    
                next_energy = curr_energy - 1
                if next_energy < 0:
                    continue
                    
                # Recharge instantly when stepping onto an 'R' cell
                if classroom[nr][nc] == 'R':
                    next_energy = energy
                    
                # Collect litter if stepping onto an 'L' cell
                next_mask = mask
                if classroom[nr][nc] == 'L':
                    next_mask |= (1 << litter_map[(nr, nc)])
                    
                # Pruning step: only queue the move if it gives us better 
                # energy than previously recorded for this (cell, mask) state.
                if next_energy > visited[nr][nc][next_mask]:
                    visited[nr][nc][next_mask] = next_energy
                    queue.append((nr, nc, next_energy, next_mask, moves + 1))
                    
        return -1

