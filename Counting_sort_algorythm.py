def counting_sort(arr):
    # Find the maximum element in the input array to determine the range.
    max_element = max(arr)
    
    # Create a counting array with a size equal to the maximum element plus one.
    count_array = [0] * (max_element + 1)

    # Count the occurrences of each element in the input array.
    for num in arr:
        count_array[num] += 1

    # Reconstruct the sorted array from the counting array.
    sorted_array = []
    for i in range(max_element + 1):
        sorted_array.extend([i] * count_array[i])

    return sorted_array

# Example usage:
my_list = [4, 2, 2, 8, 3, 3, 1]
sorted_list = counting_sort(my_list)
print(sorted_list)
