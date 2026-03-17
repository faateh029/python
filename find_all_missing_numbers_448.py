# def find_all_missing_numbers (nums):
#     n = len(nums)
#     missing_numbers = []
#     for i in range(0 , n):
#             index = abs(nums[i])
#             if(nums[index-1]>0):
#                 nums[index-1] = nums[index-1]*-1
#     for i in range(0,n):
#             if nums[i]>0:
#                 missing_numbers.append(i+1)
#     return missing_numbers


def find_all_missing_numbers(nums):
    set_nums= set(nums)
    missing_numbers = []
    for i in range(1,len(nums)+1):
        if i not in set_nums:
            missing_numbers.append(i)
    return missing_numbers
nums = [4,3,2,7,8,2,3,1]
print(find_all_missing_numbers(nums))