from typing import Union

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> Union[tuple, None]:
        lookup = {}

        for index, num in enumerate(numbers):
            complement = target - num
            if complement in lookup:
                return (
                    lookup[complement], index
                )
            
            lookup[num] = index
            
        return None

if __name__ == "__main__":
    solution = Solution()
    answer = solution.twoSum(
        numbers=[2, 7, 11, 15],
        target=9
    )
    print(answer)