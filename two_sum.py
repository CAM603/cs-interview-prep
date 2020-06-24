def two_sum(nums, target):

    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if nums[i] + nums[j] == target and i != j:
    #             return [i, j]
    cache = {}
    for i, j in enumerate(nums):
        # is the sum compliment in the dict?
        if target - j in cache:
            return [cache[target - j], i]
        cache[j] = i


print(two_sum([2, 7, 11, 15], 9))
