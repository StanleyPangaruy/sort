
def partition(nums, low, high):
    
    #sets the rightmost element as pivot
    pivot = nums[high]

    #pointer for greater element
    i = low - 1

    #compare each element with pivot
    for j in range(low, high):
        if nums[j] <= pivot:

            #if the element is smaller than the pivot
            #swap with the greater element pointed by i
            i = i + 1

            #swapping element at i with j
            (nums[i], nums[j]) = (nums[j], nums[i])

    #swap the pivot element with the greater element indicated by 1
    (nums[i+1], nums[high]) = (nums[high], nums[i+1])

    #returns the position where partition is done
    return i+1



def quickSort(nums, low, high):
    if low < high:

        #makes the elements that are
        #smaller are on the left while
        #greater are on the right
        pi = partition(nums, low, high)

        #Recursive call on the left of pivot
        quickSort(nums, low, pi-1)

        #Recursive call on the right of pivot
        quickSort(nums, pi+1, high)

nums = [46, 4, 49, 52, 19, 90, 2, 81, 38, 98]
print(nums)

size = len(nums)
quickSort(nums, 0, size - 1)

print(nums)