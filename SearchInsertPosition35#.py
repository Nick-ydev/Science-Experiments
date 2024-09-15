nums = [1,3,5,6]
target = 2

if target in nums:
    for i in range(0,len(nums)):
        if target == nums[i]:
            output = i
else: 
    for i in range(0,len(nums)):
        while nums[i] < target:
            output = i
            break

print(output)
