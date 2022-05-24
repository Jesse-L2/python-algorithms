"""
Binary Search of an already sorted list. Binary Search functions like looking up a number in a phone book with the
numbers already sorted. You first check the middle number of the array or list and then decide if the number is less
than, greater than, or equal to the target number. If the number is equal, you return the result immediately. Otherwise,
perform a similar halving of the data set on the side of the array that the target lies and repeat this process until
the target is found, or it is determined that the number is not contained in the array.

"""

def binarySearch(target, sorted_array):
    left = 0  # index
    right = len(sorted_array) - 1  # (index - 1) because we are 0 indexed
    while left <= right:
        midpoint = (left + right) // 2
        if target == sorted_array[midpoint]:
            return midpoint
        elif target < sorted_array[midpoint]:
            right = midpoint - 1
        else:  # target > sorted_array[midpoint]
            left = midpoint + 1
    return -1  # did not find target

"""
binarySearch Notes: Worst case scenario when target is not in list because the entire list is checked over making the
worst case scenario the number of times that the list can be halved making the complexity O(log(n)). Binary Search
performs extremely well on large data sets, but has the additional cost of storing subsets of the list in memory.
"""