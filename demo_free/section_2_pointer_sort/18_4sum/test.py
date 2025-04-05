def four_sum(numbers: list[int], target: int):
    numbers.sort()
    res = []

    for i in range(len(numbers)):

        if i > 0 and numbers[i] == numbers[i-1]:
            continue

        for j in range(i + 1, len(numbers)):

            if j > 0 and numbers[j] == numbers[j-1]:
                continue

            left, right = j + 1, len(numbers) - 1

            while left < right:
                total = numbers[i] + numbers[j] + numbers[left] + numbers[right]

                if total == target:
                    res.append(
                        [i, j, left, right]
                    )
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return res

