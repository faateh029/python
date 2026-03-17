#Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
#def missingNumber(nums):
    # n = len(nums)
    # new_arr = list(range(n+1))
    # for i in range(0,len(new_arr)):
    #     if new_arr[i] not in nums:
    #         return new_arr[i]
    # return -1

def missingNumber( nums):
    n = len(nums)
    sum_of_new_arr  = n*(n+1)/2
    nums_sum = 0 
    for i in range(0 , len(nums)):
        nums_sum = nums_sum+ nums[i]
    missing_number = sum_of_new_arr-nums_sum
    return missing_number


nums =[0,1]
number = missingNumber(nums)
print(number)



    #note:
          #If length = n+1 → use L(L-1)/2
          #If length = n → use n(n+1)/2