
def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums [j] == target:
                    return [i, j]
        return[]

def twoSum_hashmap(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return (num_dict[complement], i)
        num_dict[num] = i
    return []

print(twoSum_hashmap([2, 7, 11, 15], 9))