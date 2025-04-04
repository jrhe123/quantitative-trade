def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    # Step 1: 按结束时间升序排列
    intervals.sort(key=lambda x: x[1])

    # Step 2: 遍历选择不重叠区间
    end = intervals[0][1]
    count = 1  # 已选中区间数

    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            end = intervals[i][1]
            count += 1

    # Step 3: 用总数减去最多能保留的不重叠区间数
    return len(intervals) - count

# 输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
# 输出: 1
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。

# 输入: intervals = [[1,2],[1,2],[1,2]]
# 输出: 2

# 输入: intervals = [[1,2],[2,3]]
# 输出: 0