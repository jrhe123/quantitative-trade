from collections import deque, defaultdict

# [course, prereq]
# [1, 0]
# [2, 0]
# [2, 1]
# [3, 2]


# numbers = [1, 2, 2, 3, 4, 4, 4, 5]
# num_differences = len(set(numbers))
# print(num_differences)  # Output: 5


class Solution:
    def bfs(self, number_of_courses: int, courses: list[list[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * number_of_courses

        for course, prereq in courses:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque([
            i for i in indegree if i == 0
        ])

        print("graph: ", graph)
        print("indegree: ", indegree)
        print("queue: ", queue)

        count = 0

        while queue:
            course = queue.popleft()
            count += 1

            for c in graph[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)
        
        return count == number_of_courses


if __name__ == "__main__":
    solution = Solution()
    ans = solution.bfs(
        number_of_courses=4,
        courses=[
            [1, 0],
            [2, 0],
            [2, 1],
            [3, 2],
        ]
    )
    print(ans)