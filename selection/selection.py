def sort(nums):

    for i in range(9):
        minpos = i
        for j in range(i,10):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)


nums = [46, 4, 49, 52, 19, 90, 2, 81, 38, 98]
print("Selection Sort")
print(nums)
sort(nums)