import numpy as np

# Set the seed to make the output deterministic
np.random.seed(0)

# Generate a random array
arr = np.random.randint(1, 1000, size=(1, 1000))

# Sort the array: for binary search to work correctly, the array must be sorted
arr1 = np.sort(arr[0])
# print(arr1)

# Target value to find
target = 999

# Initialize binary search boundaries
start = 0
end = len(arr1) - 1

# Binary Search Logic
found = False
while start <= end:
    mid = start + (end - start) // 2  # Calculate the middle index
    if arr1[mid] == target:
        print(f"Target {target} found at index {mid}")
        found = True
        break
    elif arr1[mid] < target:
        start = mid + 1  # Move the start boundary to the right
    else:
        end = mid - 1  # Move the end boundary to the left

if not found:
    print(f"Target {target} not found in the array.")
