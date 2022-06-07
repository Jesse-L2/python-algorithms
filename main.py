"""
pythonSortingAlgorithms is an open source repository for popular sorting algorithms in Python containing detailed notes
about each step in the sorting process.
"""
# arr_1 and arr_2 are test arrays to check sorting algorithm functionality
arr_1 = [31, 41, 49, 3, 26, 11, 41, 48]
arr_2 = [7, 5, 2, 4, 6, 1, 3, 9, 8, 4]  # note there are 2 4's to check edge case of having duplicates in array


# Implementation for function for Insertion Sort
def insertion_sort(array):
    # Iterate through the array from 1 to length of the array (arr[n]) in ascending order
    for i in range(1, len(array)):

        current_position = array[i]  # this starts at 1 and will hold the value that j+1 will become allowing for swap

        # Move the elements of the array [0... i - 1] that are greater than the key to one position ahead of their
        # current position
        j = i - 1  # set j equal to the position before i

        while j >= 0 and current_position < array[j]:  # compare the current key value to the value before it
            """
            If an element is larger than the previous value, we continue to the next value setting it as current_position
            If the current value < the value before it, then move the larger element up one space
            Basically shift all elements to the right to create the position for the unsorted element
            """

            array[j + 1] = array[j]  # moving j one position to the right
            j -= 1  # decrementing j by one moves us one position to the left, letting us check the next element

        array[j + 1] = current_position  # Insert the unsorted element into the correct position

    return array


# print(insertion_sort(arr_2))

"""
Insertion Sort Notes:
Time Complexity - O(n^2)
Space Complexity - O(n)
Useful when the number of elements in an array or list is small or only a few elements are in an unsorted location
Best case scenario: array already in sorted order making Time Complexity O(n)
Worst case scenario: array in reverse sorted order making Time Complexity O(n^2). Specifically has a quadratic runtime
of an^2 + bn + c, though the bn and c elements are negligible at high values of n compared to n^2.
"""

"""
reverse_insertion_sort functions the same as the above insertion sort, except we change the sign of the second
argument in the while loop to 'current_position > array[j]'. This checks if the current value is greater than the value
before it rather than less than the preceding value, otherwise the algorithm functions the same. 
"""


# Implementation for function for Insert Sort in reverse order
def reverse_insertion_sort(array):
    for i in range(1, len(array)):
        current_position = array[i]
        j = i - 1

        while j >= 0 and current_position > array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = current_position

    return array


"""
Merge-sort is an optimal sorting algorithm that can be accomplished with a divide-and-conquer strategy. Merge-sort
will always go through the full sorting process regardless of how ordered the initial array is so it may not always be
the fastest option for small arrays. 
First, compute the midpoint and divide the subarray into two sub-arrays, each of half the size of the original. 
Second, recursively sort each of the newly created sub-arrays.
Third, merge the two sorted sub-arrays to produce the fully sorted array.
"""


# Implementation for function for Merge Sort
def merge_sort(array):
    # If len(array) == 1 or 0, the array is already sorted -> base case
    # We will only sort if there are at least 2 elements in the array
    if len(array) > 1:
        # Find the midpoint of the array
        mid = len(array) // 2  # Floor division used because we could end up with half an element on each side with '/'
        # Divide the array into two sub-arrays

        left = array[:mid]  # Slice up to midpoint
        right = array[mid:]  # Slice from midpoint to end

        # Sort the two array halves (recursion), each merge_sort() call sends us back to the beginning of the function
        merge_sort(left)
        merge_sort(right)
        # At the end of this step, we have every element in an individual array by themselves

        # Merge the two arrays
        i = 0  # index of left-most element in left array
        j = 0  # index of left-most element in right array
        k = 0  # index of left-most element of merged array

        while i < len(left) and j < len(right):
            # If the left value in the left array is less than the left value in the right array,
            # add left value to merged
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1  # increment i to check the next value in left array
            else:  # left value of left array is equal or greater than the left value of right array
                array[k] = right[j]
                j += 1  # increment j to check the next value in right array
            k += 1  # we want to increment k every time that way we don't overwrite our array

        while i < len(left):  # Checking if the left array is still incomplete
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):  # Checking if the right array is still incomplete
            array[k] = right[j]
            j += 1
            k += 1

    return array


"""
Time Complexity - O(nlog(n)) because we repeatedly divide the array into halves and it takes linear time to merge each 
of those halves. 
Space Complexity - O(n) for the temporary array 
Useful when sorting a large amount of elements or for sorting linked lists because the linked lists won't require extra
space.
Best case scenario: O(nlog(n)) - unfortunately we still have to check each element against each other so there is no 
speed boost available in the case that the list is already sorted
Worst case scenario: O(nlog(n)). 
Generally merge sort is  relatively slow for small arrays. 
"""

"""
Bubble sort starts at the beginning of a list and compares pairs of data items as it moves to the end.
If a pair of items are out of order, they are swapped, effectively bubbling large items to the end of the list.
The bubble sort algorithm then repeats the process until the list is sorted.
"""


def bubbleSort(arr):
    n = len(arr)
    while n > 1:  # Do n - 1 bubbles
        i = 1  # Start the bubble
        while i < n:
            if arr[i] < arr[i - 1]:  # If the element in question is less than the item to the left, swap
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i += 1
        n -= 1
    return arr


"""
Time complexity of O(n^2). Some minor improvements can be made to the best case scenario by 
implementing a boolean flag that checks whether no swaps occurred on a run and returning the list immediately after one
run if that is the case. 
"""

"""
Quicksort - 
1) Select the item at the list's midpoint which we will call the pivot.
2) Partition the items in the list so that all items less than the pivot are moved to the left of the pivot and do the
same so that all items greater than the pivot are moved to the right. The final position of the pivot varies depending
on the items in the list. Wherever the pivot ends up, that is its final position in the sorted list, we don't need to
move it.
3) Divide and conquer. Reapply the process recursively to the sublists formed by splitting the list at the pivot. One
sublist consists of all items to the left of the pivot and the other all the items to the right.
4) The process terminates each time it encounters a sublist with fewer than 2 items
Time complexity - O(n^2) worst case, O(n log n) best case because we go through n elements and subdivide into log n
Memory complexity - O(n) worst case, O(log n) best case
Performance can vary heavily depending on what value is chosen as the pivot, thus to avoid poor performance, it can be 
advantageous to select a random position or a median value of first/middle/last elements as the start location
"""


def quickSort(arr):  # Recursive solution
    n = len(arr)
    # Establish base case
    if n < 2:
        return arr
    # if not base case, quicksort can be easily implemented in Python with list comprehensions by subdividing into 2
    # lists with one being values less than or equal to the pivot and the other being greater than the pivot
    # and then returning the two sides of those lists recursively with the pivot in the middle and exiting on base case
    else:
        pivot = arr[0]  # Select first element of arr as pivot
        lesser_values = [i for i in arr[1:] if i <= pivot]
        greater_values = [i for i in arr[1:] if i > pivot]
        return quickSort(lesser_values) + [pivot] + quickSort(greater_values)  # Recursive call


def regularQuickSort(arr):  # Quicksort without list comprehensions
    lesser_numbers = []
    equals_pivot = []
    greater_numbers = []

    if len(arr) >= 2:
        pivot = arr[0]  # Select first element of arr as pivot
        for element in arr:
            if element < pivot:
                lesser_numbers.append(element)
            elif element > pivot:
                greater_numbers.append(element)
            elif element == pivot:
                equals_pivot.append(element)
        # join our subgroups and continue sorting if needed
        return regularQuickSort(lesser_numbers) + equals_pivot + regularQuickSort(greater_numbers)

    # if arr has 1 or 0 elements
    else:
        return arr


def quickSortWithPartition(arr, start=0, end=None):
    """In-place Quicksort (no added memory required)"""

    def qSort(arr, start=0, end=None):
        if start < end:
            pivot = partition(arr, start, end)
            qSort(arr, start, pivot - 1)  # Perform quicksort on the left side of the pivot
            qSort(arr, pivot + 1, end)  # Perform quicksort on the right side of the pivot

    def partition(arr, start=0, end=None):
        pivot = start
        i = start + 1
        for j in range(start + 1, end + 1):
            if arr[j] < arr[pivot]:  # If the element at pos i is less than or equal to first value
                arr[i], arr[j] = arr[i], arr[j]  # Perform swap
                i += 1  # Move i pointer to the right by 1
        arr[i - 1], arr[start] = arr[start], arr[i - 1]  # Swap start and pivot
        return pivot



    return qSort(arr, start, end)


print(quickSortWithPartition(arr_1, 0, len(arr_1) - 1))
