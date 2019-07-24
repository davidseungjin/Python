def merge_sort(numbers, i, k):
   if i < k:
      j = (i + k) // 2              # Find midpoint 
      merge_sort(numbers, i, j)     # Sort left part
      merge_sort(numbers, j + 1, k) # Sort right part
      merge(numbers, i, j, k)       # Merge parts
