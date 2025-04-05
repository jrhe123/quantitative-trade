class Solution:
    def three_sums(self, numbers: list[int]):
        numbers.sort()
        res = []

        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue

            left, right = i + 1, len(numbers) - 1
            while left < right:
                sum = numbers[i] + numbers[left] + numbers[right]
                if sum == 0:
                    res.append(
                        [i, left, right]
                    )
                    while left < right and numbers[left] == numbers[left + 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1


if __name__ == "__main__":
    solution = Solution()
    ans = solution.three_sums(
        numbers=[-1, 0, 1, 2, -1, -4]
    )
    print(ans)