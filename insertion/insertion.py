
def insertionSort(nums):

    for step in range(1, len(nums)):
        key = nums[step]
        j = step - 1

        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j = j-1
        
        nums[j+1] = key
        print(nums)


nums = [46, 4, 49, 52, 19, 90, 2, 81, 38, 98]
print("Insertion Sort")
print(nums)
insertionSort(nums)