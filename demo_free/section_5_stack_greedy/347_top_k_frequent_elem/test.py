from collections import Counter
import heapq

class Solution:
    def find_top_k_frequency(self, numbers: list[int], k: int) -> list[int]:
        counter = Counter(numbers)

        print("items: ", counter.items())
        # dict_items([(1, 3), (2, 2), (3, 1)])
        
        top_k = heapq.nlargest(
            k,
            counter.items(),
            key=lambda x: x[1]
        )

        print("top_k: ", top_k)
        return [num[0] for num in top_k]


# Input:
# nums = [1,1,1,2,2,3]
# k = 2

# Output:
# [1, 2]

if __name__ == "__main__":
    solution = Solution()
    ans = solution.find_top_k_frequency(
        numbers=[10,10,10,2,2,3],
        k=2
    )
    print(ans)