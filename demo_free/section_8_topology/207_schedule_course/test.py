from collections import defaultdict, deque

# course, prereq
# [1, 0]
# [2, 1]
# [3, 0]
# [3, 2]

class Solution:
    def can_finish(self, number_of_courses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * number_of_courses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        print("graph: ", graph)
        print("indegree: ", indegree)

        queue = deque(
            [i for i in range(number_of_courses) if indegree[i] == 0]
        )
        count = 0
        print("queue: ", queue)

        while queue:
            course = queue.popleft()
            count += 1

            for neighor in graph[course]:
                indegree[neighor] -= 1
                if indegree[neighor] == 0:
                    queue.append(neighor)

        return count == number_of_courses

# graph:  defaultdict(<class 'list'>, {0: [1, 3], 1: [2], 2: [3]})
# indegree:  [0, 1, 1, 2]
# queue:  deque([0])
# ans:  True

if __name__ == "__main__":
    solution = Solution()
    ans = solution.can_finish(
        4, [[1, 0], [2, 1], [3, 0], [3, 2]]
    )
    print("ans: ", ans)