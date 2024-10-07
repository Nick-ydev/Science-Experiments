nums = [5,7,7,8,8,9,9,10]

target = 9
out_list = []

count = nums.count(target)

if target in nums:
    for i in range(0, len(nums)):
        if nums[i] == target:
            out_list.append(i)
            out_list.append(count + i -1)
            break
else: out_list = [-1,-1]

print(out_list)

'''
def target_finder(list_1,target_num):
    for i in range(0,len(list_1)):
        checker = list_1[i]
        if checker == target_num:
            out_list.append(i)
    return out_list

if target in nums:
    print(target_finder(nums,target))
else: 
    out_list = [-1,-1]
    '''