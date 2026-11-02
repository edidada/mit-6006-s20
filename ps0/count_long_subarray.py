def count_long_subarray(A):
    """Count longest strictly increasing contiguous subarrays in O(n) time."""
    if not A:
        return 0
    longest = current = count = 1
    for index in range(1, len(A)):
        current = current + 1 if A[index - 1] < A[index] else 1
        if current > longest:
            longest, count = current, 1
        elif current == longest:
            count += 1
    return count
