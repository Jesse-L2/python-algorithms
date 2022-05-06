arr_1 = [31, 41, 49, 3, 26, 11, 41, 48]
arr_2 = [7, 5, 2, 4, 6, 1, 3, 9, 8, 4]  # note there are 2 4's to check edge case of having duplicates in array


# Function for Insertion Sort
def insertion_sort(array):
    # Iterate through the array from 1 to length of the array (arr[n]) in ascending order
    for i in range(1, len(array)):

        current_value = array[i]  # this starts at 1 and will hold the value that j+1 will become allowing for swap

        # Move the elements of the array [0... i - 1] that are greater than the key to one position ahead of their
        # current position
        j = i - 1  # set j equal to the position before i

        while j >= 0 and current_value < array[j]:  # compare the current key value to the value before it
            """
            If an element is larger than the previous value, we continue to the next value setting it as current_value
            If the current value < the value before it, then move the larger element up one space
            Basically shift all elements to the right to create the position for the unsorted element
            """

            array[j + 1] = array[j]  # moving j one position to the right
            j -= 1  # decrementing j by one moves us one position to the left, letting us check the next element

        array[j + 1] = current_value  # Insert the unsorted element into the correct position

    return array


# print(insertion_sort(arr_2))

"""
Notes:
Time Complexity O(n^2)
Space Complexity O(n)
Useful when the number of elements in an array or list is small or only a few elements are in an unsorted location
Best case scenario: array already in sorted order making Time Complexity O(n)
Worst case scenario: array in reverse sorted order making Time Complexity O(n^2). Specifically has a quadratic runtime
of an^2 + bn + c, though the bn and c elements are negligible at high values of n compared to n^2.
"""


# Implementation for function for Insert Sort in reverse order
def reverse_insertion_sort(array):
    pass


# Implementation for function for Merge Sort
"""
Merge-sort is an optimal sorting algorithm that can be accomplished with a divide-and-conquer strategy. 
First, compute the midpoint and divide the subarray into two subarrays, each of half the size of the original. 
Second, recursively sort each of the newly created subarrays.
Third, merge the two sorted sub-arrays to produce the fully sorted array.
"""


def merge_sort(array):
    # If len(array) == 1 or 0, the array is already sorted -> base case
    # We will only sort if there are at least 2 elements in the array
    if len(array) > 1:
        # Find the midpoint of the array
        mid = len(array) // 2  # Floor division used because we could end up with half an element on each side with '/'
        # Divide the array into two sub-arrays

        left = array[:mid]  # Slice up to midpoint
        right = array[mid:]  # Slice from midpoint to end

        # Sort the two array halves (recursion)
        merge_sort(left)
        merge_sort(right)

        # Merge the two arrays
        i = 0  # index of left-most element in left array
        j = 0  # index of left-most element in right array
        k = 0  # index of left-most element of merged array

        while i < len(left) and j < len(right):
            # If the left value in the left array is less than the left value in the right array,
            # add left value to merged
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:  # left value of left array is equal or greater than the left value of right array
                array[k] = right[j]
                j += 1
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


print(merge_sort(arr_2))
"""
Time Complexity O(nlog(n))
Space Complexity 
Useful when 
Best case scenario: 
Worst case scenario: 
"""
