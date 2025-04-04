from collections import defaultdict, OrderedDict

class AllOne:
    def __init__(self):
        self.key_count = {}
        self.count_keys = defaultdict(OrderedDict)
        self.min_count = float('inf')
        self.max_count = 0

    def inc(self, key: str) -> None:
        cnt = self.key_count.get(key, 0)
        if cnt:
            del self.count_keys[cnt][key]
            if not self.count_keys[cnt]:
                del self.count_keys[cnt]
                if self.min_count == cnt:
                    self.min_count += 1

        cnt += 1
        self.key_count[key] = cnt
        self.count_keys[cnt][key] = None
        self.max_count = max(self.max_count, cnt)
        self.min_count = min(self.min_count, cnt) if cnt == 1 else self.min_count

    def dec(self, key: str) -> None:
        if key not in self.key_count:
            return

        cnt = self.key_count[key]
        del self.count_keys[cnt][key]
        if not self.count_keys[cnt]:
            del self.count_keys[cnt]
            if self.max_count == cnt:
                self.max_count -= 1
            if self.min_count == cnt:
                self.min_count = min(self.count_keys) if self.count_keys else float('inf')

        if cnt == 1:
            del self.key_count[key]
        else:
            cnt -= 1
            self.key_count[key] = cnt
            self.count_keys[cnt][key] = None
            self.min_count = min(self.min_count, cnt)

    def getMaxKey(self) -> str:
        if self.max_count in self.count_keys:
            return next(iter(self.count_keys[self.max_count]))
        return ""

    def getMinKey(self) -> str:
        if self.min_count in self.count_keys:
            return next(iter(self.count_keys[self.min_count]))
        return ""
    

# 设计一个支持以下操作的数据结构，所有操作都需在 O(1) 时间内完成：

# inc(key)：将 key 的计数增加 1。如果不存在则插入。

# dec(key)：将 key 的计数减少 1。如果减到 0 则从数据结构中移除。

# getMaxKey()：返回任意一个最大计数的 key（不为空）。

# getMinKey()：返回任意一个最小计数的 key（不为空）。