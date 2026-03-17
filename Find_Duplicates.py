# WE WILL WRITE DIFFERENT VARIANTS OF FINDING DUPLICATES IN AN ARRAY

#RETURN AN ARRAY WHICH CONTAINS DUPLICATES IN THE INPUT ARRAY

# def find_duplicates(nums):
#     duplicates= []
#     if len(nums)<=1:
#         return "Invalid Length"
#     for i in range(len(nums)):
#         for j in range(i+1 , len(nums)):
#             if nums[i]==nums[j] and nums[i] not in duplicates:
#                 duplicates.append(nums[i])
#     return duplicates




#Return True if there is a duplicate in the array

# def find_duplicates(nums):
#     if len(nums)<=1:
#         return "Invalid Length"
#     for i in range(len(nums)):
#         for j in range(i+1 , len(nums)):
#             if nums[i]==nums[j]:
#                 return True
#     return False


# optimized solution for finding duplicates by using sets because set is one of the 4  built in datatypes of python which isunchangeable , unordered , hetrogenous and allows no duplicates .
#others are tuples,dictionary , list
def find_duplicates(nums):
    if len(nums)<=1:
        return "invalid length"
    duplicate_finder_set = set(nums)
    if len(duplicate_finder_set)==len(nums):
        return False
    return True

numArr = [1,2,3,4,5]
result = find_duplicates(numArr)
print(result)