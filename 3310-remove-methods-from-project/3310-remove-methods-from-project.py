class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Build the adjacency list for the invocation graph
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)
            
        # Step 2: Use BFS or DFS to identify all suspicious methods starting from k
        suspicious = [False] * n
        suspicious[k] = True
        queue = [k]
        
        while queue:
            curr = queue.pop(0)
            for neighbor in graph[curr]:
                if not suspicious[neighbor]:
                    suspicious[neighbor] = True
                    queue.append(neighbor)
                    
        # Step 3: Check if any non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                # If an external method calls a suspicious one, nothing can be removed
                return list(range(n))
                
        # Step 4: Return all non-suspicious methods if the group is isolated
        return [i for i in range(n) if not suspicious[i]]
