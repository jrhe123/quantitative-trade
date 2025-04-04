class StockSpanner:
    def __init__(self):
        self.stack = []  # 存放 (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
    
# next(100) → [(100, 1)] → 输出 1  
# next(80)  → [(100, 1), (80, 1)] → 输出 1  
# next(60)  → [(100, 1), (80, 1), (60, 1)] → 输出 1  
# next(70)  → 70 > 60 → 弹出60 → span=2 → [(100, 1), (80, 1), (70, 2)]  
# next(60)  → 输出 1  
# next(75)  → 75 > 60+70 → 弹出 60+70 → span=4 → 输出 4  