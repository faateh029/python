def two_sum(nums , target):
    n = len(nums)
    nums_dict={}
    for i in range(n):
        complement = target - nums[i]
        if complement in nums_dict:
            return [nums_dict[complement],i]
        else:
           nums_dict[nums[i]] = i
    return -1

print(two_sum([2,7,11,15],9))

