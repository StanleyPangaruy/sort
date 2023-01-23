
def mergeSort(nums):
    if len(nums) > 1:
        r = len(nums)//2
        left = nums[:r]
        right = nums[r:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

        print(nums)

nums = [46, 4, 49, 52, 19, 90, 2, 81, 38, 98]
print("Merge Sort")
print(nums)
mergeSort(nums)