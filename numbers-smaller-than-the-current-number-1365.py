# def smallerNumbersThanCurrent( nums):
#     arr = []
#     for i in range (len(nums)):
#         count = 0
#         for j in range (len(nums)):
#             if(nums[i]>nums[j]):
#                 count+=1
            
#         arr.append(count)
#     return arr

#more efficient solution using dictionaries o(nlogn)
def smallerNumbersThanCurrent( nums):
    sorted_nums = sorted(nums)
    ret_arr=[]
    d = {}
    nums_length = len(nums)
    for i in range(nums_length):
        if(sorted_nums[i] not in d):
            d[sorted_nums[i]]=i
    for i in range(nums_length):
        if(nums[i] in d):
            ret_arr.append(d.get(nums[i]))
    return ret_arr
    
    
print(smallerNumbersThanCurrent([5,3,10,2,9,4]))