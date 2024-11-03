"""
Author: Ved Vyas
Co-Author / Exercise provided by: University of Alberta CMPUT 175 Course Team & Instructors (2023)
Functionality of code: In this code, I've implemented two different recursive sorting algorithms - 
selection sort and merge sort. Both of these sort the numbers in descending order. What's really cool 
about this implementation is that I get to compare how these two algorithms perform with different 
types of input data (random numbers, already sorted ascending, and already sorted descending). I've 
always been fascinated by how different sorting algorithms perform, and this exercise let me see 
that firsthand through actual timing measurements.
"""

# I'm importing these modules to help with generating random numbers and measuring execution time
import random
import time

def recursive_selection_sort(data, data_len, index=0):
    """My implementation of recursive selection sort that sorts in descending order"""
    # My base case - if I've reached the end of the list, I'm done sorting
    if index == data_len - 1:
        return

    # I'm keeping track of where my current minimum value is
    min_index = index
    
    # I loop through the remaining unsorted portion to find the largest number
    for i in range(index + 1, data_len):
        if data[i] > data[min_index]:
            min_index = i

    # If I found a larger number, I swap it with my current position
    if min_index != index:
        data[index], data[min_index] = data[min_index], data[index]

    # I recursively sort the rest of the list
    recursive_selection_sort(data, data_len, index + 1)

def recursive_merge_sort(data):
    """My implementation of recursive merge sort that sorts in descending order"""
    # My base case - if the list has 1 or fewer elements, it's already sorted
    if len(data) <= 1:
        return data

    # I'm splitting my list into two halves
    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]

    # I recursively sort both halves
    left_half = recursive_merge_sort(left_half)
    right_half = recursive_merge_sort(right_half)

    # I merge my sorted halves back together
    return merge(left_half, right_half)

def merge(left, right):
    """My helper function to merge two sorted lists while maintaining descending order"""
    # I initialize my result list and indices
    result = []
    left_index = right_index = 0

    # I compare elements from both lists and add the larger one to my result
    while left_index < len(left) and right_index < len(right):
        if left[left_index] >= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # I add any remaining elements from either list
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

if __name__ == "__main__":
    # I'm creating my test data - a list of 500 random numbers
    random_list = [random.randint(1, 1000) for i in range(500)]
    list_len = len(random_list)
    
    # I'm also creating sorted versions to test different scenarios
    ascending_list = sorted(random_list)
    descending_list = sorted(random_list, reverse=True)

    # First, I'm testing with random numbers
    random_list_ = random_list.copy()  # I make a copy to preserve the original
    start_sel = time.time()
    recursive_selection_sort(random_list_, list_len)
    end_sel = time.time()

    start_merge = time.time()
    recursive_merge_sort(random_list)
    end_merge = time.time()

    # I'm printing my results for random numbers
    print('The execution time to sort a random list of integers in descending order:')
    print(' - Recursive selection sort:', end_sel - start_sel)
    print(' - Recursive merge sort:', end_merge - start_merge)

    # Now I'm testing with already sorted ascending numbers
    ascending_list_ = ascending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(ascending_list_, list_len)
    end_sel = time.time()

    start_merge = time.time()
    recursive_merge_sort(ascending_list)
    end_merge = time.time()

    # I'm printing my results for ascending numbers
    print('The execution time to sort an ascending list of integers in descending order:')
    print(' - Recursive selection sort:', end_sel - start_sel)
    print(' - Recursive merge sort:', end_merge - start_merge)

    # Finally, I'm testing with already sorted descending numbers
    descending_list_ = descending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(descending_list_, list_len)
    end_sel = time.time()

    start_merge = time.time()
    recursive_merge_sort(descending_list)
    end_merge = time.time()

    # I'm printing my results for descending numbers
    print('The execution time to sort a descending list of integers in descending order:')
    print(' - Recursive selection sort:', end_sel - start_sel)
    print(' - Recursive merge sort:', end_merge - start_merge)