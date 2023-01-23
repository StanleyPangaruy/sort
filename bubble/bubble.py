
def bubbleSort(nums):
    n = len(nums)
    swapped = False

    for i in range(n-1):
        for j in range(0, n-i-1):
            if nums[j] > nums[j + 1]:
                swapped =  True
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        if not swapped:
            return

        print(nums)

nums = [46, 4, 49, 52, 19, 90, 2, 81, 38, 98]
print(nums)
bubbleSort(nums)