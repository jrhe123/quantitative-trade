from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for dest, src in prerequisites:
            graph[src].append(dest)

        visited = [0] * numCourses  # 0 = 未访问, 1 = 正在访问, 2 = 已完成访问

        def dfs(course):
            if visited[course] == 1:  # 回到当前路径中，出现环
                return False
            if visited[course] == 2:  # 已经检查过，无需再DFS
                return True

            visited[course] = 1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            visited[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
