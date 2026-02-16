# USACO 2020 December Contest Bronze #1: Do You Know Your ABCs?

nums = input().split()

for i in range(len(nums)):
    nums[i] = int(nums[i])

nums.sort()

ABC = int(nums[-1])

A = nums[0]
B = nums[1]
C = ABC - A - B

print(A, B, C)