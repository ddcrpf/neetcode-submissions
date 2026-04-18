class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        inf = 2147483647
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r,c = queue.popleft()
            for i, j  in directions:
                ir , jc = r + i , c + j

                if ir < 0 or jc < 0 or ir > (rows-1) or jc > (cols-1):
                    continue

                if grid[ir][jc] == inf:
                    grid[ir][jc] = grid[r][c] + 1
                    queue.append((ir, jc))



        # [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]




# [inf, -1 , 0 , 1]
# [inf, inf, 1, -1]
# [1, -1 , inf, -1]
# [0. , -1 , inf, inf]

# [(0,2), (3,0)]

# for r in rows:
#     for c in cols:
#         if grid[r][c] = 0
# [(1,0), (-1,0), (0,1), (0,-1)]

# in queue:
# (0,2)  -> (1,2) -> if INF -> 1
# (0,2) -> (0,3) -> INF -> 1 
# (0,2) -> (0,1) -> not INF -> blocked 


# (3,0) -> (2,0) -> INF -> 1
# (3,0) -> (3,1) -> blocked

# [(1,0), (-1,0), (0,1), (0,-1)]

# (1,2) -> (1,1) -> Inf -> 








