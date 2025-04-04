import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.idx_map = defaultdict(set)  # val -> set of indices

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.idx_map[val].add(len(self.nums) - 1)
        return len(self.idx_map[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.idx_map[val]:
            return False

        # 取出一个待删除的下标
        remove_idx = self.idx_map[val].pop()
        last_val = self.nums[-1]

        # 替换为最后一个元素（如果不是自己）
        self.nums[remove_idx] = last_val
        self.idx_map[last_val].add(remove_idx)
        self.idx_map[last_val].discard(len(self.nums) - 1)

        # 删除末尾元素
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# 实现一个允许元素重复的数据结构，支持以下操作，平均时间复杂度 O(1)：

# insert(val)：插入元素，返回是否为首次插入（是否首次出现）

# remove(val)：移除一个 val（若有多个只移除一个），返回是否成功

# getRandom()：返回一个随机元素，每个元素出现的概率与其出现次数成正比


