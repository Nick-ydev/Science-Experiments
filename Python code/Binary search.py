import math

nums = {3,8,25,35,38,41,44,53,60,62,93,97}
target = 25

length_nums = len(nums)
mid = length_nums/2

for i in range (1,length_nums):
    if target <= nums[mid]:
        new_mid = mid/2
