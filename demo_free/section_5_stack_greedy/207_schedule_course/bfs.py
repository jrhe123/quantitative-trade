from typing import List
from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 构建图 & 入度表
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1

        # 所有入度为0的节点入队
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        count = 0

        print("graph: ", graph)
        print("indegree: ", indegree)
        print("queue: ", queue)

        while queue:
            course = queue.popleft()
            count += 1
            print("course: ", course)
            
            for neighbor in graph[course]:
                print("neighbor: ", neighbor)
                
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses

if __name__ == '__main__':
    solution = Solution()
    answer = solution.canFinish(3, [[1,0], [2,1]])
    print(answer)