from collections import deque, defaultdict

def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    # Step 1: 构图和入度
    for course, pre in prerequisites:
        graph[pre].append(course)
        in_degree[course] += 1

    # Step 2: 找所有入度为0的课程
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    order = []

    # Step 3: 拓扑排序
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == numCourses else []


# 与 Leetcode 207 的差别：
# 207：判断有没有环

# 210：输出一个拓扑序列（若图无环）

