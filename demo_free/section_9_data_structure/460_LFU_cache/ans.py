from collections import defaultdict, OrderedDict

# Least Frequently Used (LFU) cache
class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_to_val_freq = {}  # key -> (val, freq)
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> keys (LRU)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1

        val, freq = self.key_to_val_freq[key]
        # 删除旧频率位置
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # 更新频率
        self.key_to_val_freq[key] = (val, freq + 1)
        self.freq_to_keys[freq + 1][key] = None

        return val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.key_to_val_freq:
            # 更新值并提升频率
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self.get(key)
            return

        # 淘汰
        if len(self.key_to_val_freq) >= self.cap:
            old_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[old_key]

        # 插入新元素
        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1