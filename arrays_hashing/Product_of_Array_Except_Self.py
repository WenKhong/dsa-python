def productExceptSelf(nums):
    res = [1] * len(nums)

    # res[i] = product of everything to the left of i
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    # multiply in the product of everything to the right of i
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]

    return res

print(productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
print(productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]

# Time : O(n) Space : O(1) extra (output array not counted)
