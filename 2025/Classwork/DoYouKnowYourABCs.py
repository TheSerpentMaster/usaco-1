# USACO 2020 December Contest Bronze #1: Do You Know Your ABCs?

nums = input().split()
for i in range(len(nums)):
    nums[i] = int(nums[i])
nums.sort()

ABC = int(nums[-1])

print(nums[0], nums[1], ABC - nums[0] - nums[1])