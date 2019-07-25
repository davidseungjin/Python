def merge(numbers, i, j, k):
    # Create temporary list merged_numbers
    # Initialize position variables

    # Add smallest element to merged numbers
    while left_pos <= j and right_pos <= k:
        if numbers[left_pos] <= numbers[right_pos]:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos = left_pos + 1
        else:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos = right_pos + 1
        merge_pos = merge_pos + 1
    # If left partition not empty, add remaining elements
    while left_pos <= j:
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos = left_pos + 1
        merge_pos = merge_pos + 1

    # If right partition now empty, add remaining elements
    while right_pos <= k:
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    # Copy merge number back to numbers
    for merge_pos in range(merged_size):
        numbers[i + merge_pos] = merged_numbers[merge_pos]

