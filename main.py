def firstMissingPositive(nums):
    n = len(nums)

    # Step 1: Replace negative and zero elements with n+1
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n+1

    # Step 2: Mark the presence of positive integers
    for i in range(n):
        idx = abs(nums[i])
        if idx <= n:
            nums[idx-1] = -abs(nums[idx-1])

    # Step 3: Find the first missing positive integer
    for i in range(n):
        if nums[i] > 0:
            return i+1

    return n+1


nums1 = [1, 2, 0]
nums2 = [7, 8, 9, 11, 12]
print(firstMissingPositive(nums1))
print(firstMissingPositive(nums2))
