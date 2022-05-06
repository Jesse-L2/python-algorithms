arr_1 = [31, 41, 59, 26, 41, 48]
arr_2 = [5, 2, 4, 6, 1, 3]


# Function for Insertion Sort
def insertion_sort(array):
    # Iterate through the array from 1 to length of the array (arr[n]) in ascending order
    for i in range(1, len(array)):

        current_value = array[i]  # this starts at 1 and will hold the value that j+1 will become allowing for swap

        # Move the elements of the array [0... i - 1] that are greater than the key to one position ahead of their
        # current position
        j = i - 1  # set j equal to the position before i

        while j >= 0 and current_value < array[j]:  # compare the current key value to the value before it
            '''
            If an element is larger than the previous value, we continue to the next value setting it as current_value
            If the current value < the value before it, then move the larger element up one space
            Basically shift all elements to the right to create the position for the unsorted element
            '''

            array[j + 1] = array[j]  # moving j one position to the right
            j -= 1  # decrementing j by one moves us one position to the left, letting us check the next element

        array[j + 1] = current_value  # Insert the unsorted element into the correct position

    return array


# print(insertion_sort(arr_2))

''' 
Notes:
Time Complexity O(n^2)
Space Complexity O(n)
Useful when the number of elements in an array or list is small or only a few elements are in an unsorted location
'''

def reverse_insertion_sort(array):
    pass

def merge_sort(array):
    pass