def containsDuplicate(nums):
    cache = {}
    for num in nums:
        if not num in cache:
            cache[num] = 1
        else:
            return True
    return False


print(containsDuplicate([1, 2, 3, 4, 5]))
print(containsDuplicate([1, 2, 3, 4, 5, 1]))
