# 풀이 1
"""from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            queue = deque()
            queue.append((i, j))
            grid[i][j] = 0

            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                        if grid[nx][ny] == '1':
                            grid[nx][ny] = 0
                            queue.append((nx, ny))
                    else:
                        continue
        cnt=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(i,j)
                    cnt+=1
        return cnt"""


"""
# 풀이 2
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return

            grid[i][j] = 0

            # 동서남북 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
        return count"""

#풀이 3
from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #self.grid =grid
        self.M=len(grid)
        self.N=len(grid[0])
        self.directions =[[0, 1], [0, -1], [1, 0], [-1, 0]]
        cnt = 0
        for i in range(self.M):
            for j in range(self.N):
                if grid[i][j]=="1":
                    self.bfs(grid,i,j)
                    cnt+=1
        return cnt
    def bfs(self,grid,i,j):
        grid[i][j] = 0
        queue=deque([(i,j)])
        while queue:
            node =queue.popleft()
            for direction in self.directions:
                node_new = (node[0]+direction[0],node[1]+direction[1])
                if self.check_val(node_new):
                    if grid[node_new[0]][node_new[1]] =="1":
                        grid[node_new[0]][node_new[1]] = 0
                        queue.append(node_new)

    def check_val(self,node):
        if 0<=node[0]<self.M and 0<=node[1]<self.N:
            return True
        else:
            return False

#풀이 4
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid =grid
        self.M=len(grid)
        self.N=len(grid[0])
        self.directions =[[0, 1], [0, -1], [1, 0], [-1, 0]]
        cnt = 0
        for i in range(self.M):
            for j in range(self.N):
                if self.grid[i][j]=="1":
                    self.bfs(i,j)
                    cnt+=1
        return cnt
    def bfs(self,i,j):
        self.grid[i][j] = 0
        queue=deque([(i,j)])
        while queue:
            node =queue.popleft()
            for direction in self.directions:
                node_new = (node[0]+direction[0],node[1]+direction[1])
                if self.check_val(node_new):
                    if self.grid[node_new[0]][node_new[1]] =="1":
                        self.grid[node_new[0]][node_new[1]] = 0
                        queue.append(node_new)

    def check_val(self,node):
        if 0<=node[0]<self.M and 0<=node[1]<self.N:
            return True
        else:
            return False


grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
"""grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]"""
sol=Solution()
print(sol.numIslands(grid))





