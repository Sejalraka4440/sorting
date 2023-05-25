def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# Example usage
numbers = [2, 4, 7, 10, 13, 15, 20, 22]
target_number = 13

result = binary_search(numbers, target_number)
if result != -1:
    print(f"Target number {target_number} found at index {result}.")
else:
    print("Target number not found.")
