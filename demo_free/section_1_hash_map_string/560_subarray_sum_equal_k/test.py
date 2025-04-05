def subarraySum(nums, k):
    prefix_count = {0: 1}
    pre_sum = 0
    count = 0

    for num in nums:
        pre_sum += num

        if pre_sum - k  in prefix_count:
            count += prefix_count[pre_sum - k]

        prefix_count[pre_sum] = prefix_count.get(pre_sum, 0) + 1

    return count


subarraySum(
    [1,1,1], 2
)