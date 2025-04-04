def removeCoveredIntervals(intervals):
    # 起点升序，终点降序
    intervals.sort(key=lambda x: (x[0], -x[1]))

    count = 0  # 非覆盖区间计数
    end = 0    # 当前最大终点

    for start, stop in intervals:
        # 当前区间不被覆盖
        if stop > end:
            count += 1
            end = stop  # 更新最大终点
        # 否则被前面的区间覆盖，跳过

    return count


# 输入：intervals = [[1,4],[3,6],[2,8]]
# 输出：2
# 解释：[1,4] 被 [2,8] 覆盖了
