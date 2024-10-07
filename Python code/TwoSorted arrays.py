
nums1 = [1,3]
nums2 = [2]

nums1.extend(nums2)
print(nums1)

nums1.sort()
print(nums1)
n_obs = len(nums1)
print(n_obs,"Obs")
if n_obs % 2 == 0: #even
    median = (((nums1[int(n_obs/2)]) + (nums1[int(n_obs/2)-1]))/2)
else:
    median = nums1[int(n_obs /2)]

print(median)