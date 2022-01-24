nums = []
n = 50
for i in range(2, n+1):
    nums.append(i)
x = True
while x:
    for i in nums:
        for j in nums[nums.index(i)+1:]:
            if j % i == 0:
                nums.remove(j)
    else:
        x = False
print(nums)

'''

Ans => [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
Space Complexity => O(n)

'''
