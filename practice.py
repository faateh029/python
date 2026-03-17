

# nums = [5, 2, 9, 1]
# new_list = sorted(nums)
# print(new_list)
# print(nums.sort(reverse=True))
# print(nums)
# nums.sort()
# print(nums)
# new_list2= sorted(nums,reverse=True)
# print(new_list2)

# names = ["Fatih", "Ali", "Zara"]
# print(sorted(names))

# words = ["apple", "kiwi", "banana"]
# words.sort(key=len)
# print(words)

# pairs = [(2,6), (2,6), (3,3)]
# pairs.sort(key=lambda x: x[1])
# print(pairs)
# #sort by first element , if first element is same then sort by second element
# pairs.sort(key = lambda x: (x[0] , x[1]))

# print(pairs)

# #dictionaries time complexity Search → O(1)
# Insert → O(1)
# Delete → O(1)

from collections import Counter
nums = [1,2,2,3,1,2]
freq = Counter(nums)
# for num in nums:
#     if num in freq:
#         freq[num]+=1
#     else:
#         freq[num]=1
print(freq)        