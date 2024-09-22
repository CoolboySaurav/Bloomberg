pos = 0
for j in range(1, len(nums)):
if nums[pos] != nums[j]:
pos += 1
nums[pos] = nums[j]
return pos + 1