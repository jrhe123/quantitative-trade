class Solution:
    def three_sums(self, numbers: list[int]):
        numbers.sort()
        res = []
        n = len(numbers)

        for i in range(n):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue

            left, right = i+1, n-1
            while left < right:
                s = numbers[left] + numbers[i] + numbers[right]
                if s == 0:
                    res.append(
                        [numbers[left], numbers[i], numbers[right]]
                    )
                    while left < right and numbers[left] == numbers[left+1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return res


if __name__ == "__main__":
    solution = Solution()
    ans = solution.three_sums(
        numbers=[-1, 0, 1, 2, -1, -4]
    )
    print(ans)