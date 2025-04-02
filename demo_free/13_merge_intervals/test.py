# [[1,3],[2,6],[8,10],[15,18]]

# => [[1,6],[8,10],[15,18]]

class Solution:
    def merge_intervals(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        res = [
            intervals[0]
        ]

        for current in intervals[1:]:
            last = res[-1]

            if current[0] < last[1]:
                last[1] = max(last[1], current[1])
            else:
                res.append(current)
        
        return res



if __name__ == "__main__":
    solution = Solution()
    ans = solution.merge_intervals(
        [[1,3],[2,6],[15,18], [8,10]]
    )
    print("ans: ", ans)