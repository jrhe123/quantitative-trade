def subarraysDivByK(nums, k):
    prefix_count = {0: 1}
    pre_sum = 0
    count = 0

    for num in nums:
        pre_sum += num
        mod = pre_sum % k

        count += prefix_count.get(mod, 0)

        prefix_count[mod] = prefix_count.get(mod, 0) + 1
    
    return count