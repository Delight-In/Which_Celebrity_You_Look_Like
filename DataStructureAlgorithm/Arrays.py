import array

# Create an array of integers (type 'i' for signed integers)
arr = array.array('i', [1, 2, 3, 4, 5])
print(arr)

# Append an element
arr.append(6)
print(arr)  # Output: array('i', [1, 2, 3, 4, 5, 6])

# Insert an element at a specific index (index 2)
arr.insert(2, 10)
print(arr)  # Output: array('i', [1, 2, 10, 3, 4, 5, 6])

# Remove an element (first occurrence of 3)
arr.remove(3)
print(arr)  # Output: array('i', [1, 2, 10, 4, 5, 6])

# Pop an element at index 3
popped_value = arr.pop(3)
print(popped_value)  # Output: 4
print(arr)  # Output: array('i', [1, 2, 10, 5, 6])

# Delete an element by index (index 1)
del arr[1]
print(arr)  # Output: array('i', [1, 10, 5, 6])

# Delete the entire array
del arr
# print(arr)  # Uncommenting this will raise a NameError since 'arr' is deleted


# Check if an element exists in the array
print(10 in arr)  # Output: True
print(3 in arr)   # Output: False

# Find the index of a specific value
index_of_10 = arr.index(10)
print(index_of_10)  # Output: 1

# Length of the array
print(len(arr))  # Output: 4

# Reverse the array
arr.reverse()
print(arr)  # Output: array('i', [6, 5, 10, 1])

# Slice the array (get elements from index 1 to 3)
sliced_arr = arr[1:3]
print(sliced_arr)  # Output: array('i', [5, 10])

import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Append an element
arr.append(6)
print(arr)  # Output: array('i', [1, 2, 3, 4, 5, 6])

# Insert an element at index 2
arr.insert(2, 10)
print(arr)  # Output: array('i', [1, 2, 10, 3, 4, 5, 6])

# Remove the element 3
arr.remove(3)
print(arr)  # Output: array('i', [1, 2, 10, 4, 5, 6])

# Pop the element at index 3
arr.pop(3)
print(arr)  # Output: array('i', [1, 2, 10, 5, 6])

# Check if 10 is in the array
print(10 in arr)  # Output: True

# Find the index of the value 10
print(arr.index(10))  # Output: 2

# Reverse the array
arr.reverse()
print(arr)  # Output: array('i', [6, 5, 10, 2, 1])






# Numpy Array Creation Operations
import numpy as np
arr = np.array(["Mira", "Krishna", "Radha", "Priyanka"])
print(arr)

# 1.Create a NumPy array from a Python list or tuple.
L = [1, 2, 3, 4, 5]
T = (1.5, 2, 3, 4, 5)
arr1 = np.array(L)
arr2 = np.array(T)
print(arr1, arr2)

# 2.Create an array filled with zeros.
arr0 = np.zeros((2,3), dtype=np.float32)
print(arr0)

# 'x' and will have a data type of 'i4', which is a 4-byte integer (also known as int32)
a = np.zeros((2,3), dtype=[('x', 'i4'), ('y', 'i4')]) # custom dtype
print(a)

# 3. Create an array filled with ones.
array1 = np.ones((3,3), dtype = int)
print(array1)

# 4. Create an array filled with a specific value.
arrfull = np.full((5,5), 100, dtype=int)
print(arrfull)

# 5. Create an array with a range of values (similar to `range()`).
arrr = np.arange(20,100,5, dtype=float).reshape(4,4)
print(arrr)

# 6. Create an array of evenly spaced values over a specified range.
arrlin = np.linspace(1,2,10, dtype=int)
print(arrlin)

# 7. Create an identity matrix (2D array with ones on the diagonal).
arreye = np.eye(5,6, dtype=int)
print(arreye)

# 8. Create an array of random numbers between 0 and 1.
arrnd = np.random.rand(2,3)
print(arrnd)

# 9. Create an array of random numbers from a standard normal distribution.
arrn = np.random.randn(5,5)
print(arrn)

# 10. Create an array of random integers.
arrint = np.random.randint(2,3, size= (2,3,2))
print(arrint)

## Array Manipulation Operations


# 11. Change the shape of an array.
arr = np.array(["Mira", "Krishna", "Radha", "Priyanka"]).reshape(2,2)
print(arr)

# 12. Flatten a multi-dimensional array to a 1D array.
arr3d = np.linspace(1,10,30).reshape(3,2,5)
print("arr=",arr3d)
arrflat = arr3d.flatten()
print('flat=',arrflat)

# 13. Transpose a 2D array (flip rows and columns).
arrnd = np.random.rand(2,3)
print(arrnd)
print(np.transpose(arrnd))

# 14. Return a flattened 1D array, similar to `flatten()` but with a reference to the original data.
arr3d = np.linspace(1,10,30).reshape(3,2,5)
print("arr=",arr3d)
arrflat = arr3d.ravel()
# a = np.ravel(arr3d)
# print(a)
print('flat=',arrflat)

# 15. **`np.concatenate()`**: Join two or more arrays along an existing axis.
ar1 = np.array([1,2,4,6])
# ar2 = np.array(["A","B","C","D"])
ar3 = np.array([2.5,8.1,5.63,6.66])
arf = np.concatenate((ar1, ar3),axis = 0, dtype=float)
print(arf)

# 16. Split an array into multiple sub-arrays.
arrr = np.arange(20,100,5, dtype=float).reshape(4,4)
print("Array:")
print(arrr)
result = np.split(arrr, [0, 2], axis=1)
print("Split Array:")
print(result)


# 17. Stack arrays along a new axis (axis = 0 or axis = 1).
ar1 = np.array([1,2,4,6])
ar2 = np.array([2.5,8.1,5.63,6.66])
a = np.stack((ar1, ar2), axis = 1)
print(a)

# 18. Horizontally stack arrays (stack along axis 1).
ar1 = np.array([1,2,4,6])
ar2 = np.array([2.5,8.1,5.63,6.66])
a = np.hstack((ar1, ar2))
print(a)

# 19. Vertically stack arrays (stack along axis 0).
ar1 = np.array([1,2,4,6])
ar2 = np.array([2.5,8.1,5.63,6.66])
a = np.vstack((ar1, ar2))
print(a)

# 20. **`np.expand_dims()`**: Expand the dimensions of an array.
print("Normal arr")
arr = np.array(["Mira", "Krishna", "Radha", "Priyanka"])
print(arr)
print(arr.shape)
print("Expanded dim arr")
exp = np.expand_dims(arr,axis=0)
print(exp)
print(exp.shape)

# Indexing and Slicing

arr = np.array(["Mira", "Krishna", "Radha", "Priyanka"]).reshape(2,2)
print(arr[:,1])

# 21. **`arr[::2]`**: Slice an array to select every other element.
# 22. **`arr[:5]`**: Slice an array to select the first 5 elements.
# 23. **`arr[-3:]`**: Slice an array to select the last 3 elements.
# 24. **`arr[1:4]`**: Slice an array from index 1 to index 4 (excluding 4).
# 25. **`arr[::]`**: Slice the entire array (copy of the original array).
# 26. **`arr[2, 3]`**: Indexing 2D array (row 2, column 3).
# 27. **`arr[:, 1]`**: Select all rows from the second column of a 2D array.
# 28. **`arr[1, :]`**: Select the second row of a 2D array.
# 29. **`arr[1:4, 2:5]`**: Slice a sub-array from rows 1 to 4 and columns 2 to 5.

# 30. **`arr[boolean_mask]`**: Use boolean indexing to select elements based on conditions.
arr = np.array(["Mira", "Krishna", "Radha", "Priyanka"]).reshape(2,2)
print([arr=="Krishna"])
print(arr[arr!="Krishna"])


# Mathematical Operations

# 31. Element-wise addition of two arrays.
ar1 = np.array([1,2,4,6])
ar2 = np.array([2.5,8.1,5.63,6.66])
print("sum  add")
print(np.sum(ar1), np.add(ar1, ar2))

# 32. Element-wise subtraction of two arrays.
ar1 = np.array([1,2,4,6])
ar2 = np.array([2.5,8.1,5.63,6.66])
print("sub")
print(np.subtract(ar1,ar2))

# 33. Element-wise multiplication of two arrays.
ar1 = np.array([1,2,4,6])
ar2 = np.array([2.5,8.1,5.63,6.66])
print("mul")
print(np.multiply(ar1, ar2))

# 34. Element-wise division of two arrays.
ar1 = np.array([1,2,4,6])
ar2 = np.array([2.5,8.1,5.63,6.66])
print("div")
print(np.divide(ar1,ar2))

# 35. Element-wise power (raising array elements to a power).
ar1 = np.array([1,2,4,6])
ar2 = np.array([2.5,8.1,5.63,6.66])
print("power")
print(np.power(ar2, ar1))

# 36. Element-wise modulo (remainder after division).
ar1 = np.array([1,2,4,6])
ar2 = np.array([2.5,8.1,5.63,6.66])
print("mod")
print(np.mod(ar1, ar2))

# 37. Dot product of two arrays (vectors or matrices).
ar1 = np.array([1,2,4,6])
ar2 = np.array([2.5,8.1,5.63,6.66])
print("dot")
print(np.dot(ar1, ar2))

# 38. Sum of all elements in an array.
ar1 = np.array([1,2,4,6])
ar2 = np.array([2.5,8.1,5.63,6.66])
print(np.sum(ar1), np.sum(ar2))

# 39. **`np.mean()`**: Mean (average) of the elements in an array.
ar1 = np.array([1,2,4,6])
ar2 = np.array([2.5,8.1,5.63,6.66])
print(np.mean(ar1))

# 40. **`np.std()`**: Standard deviation of the elements in an array.
ar1 = np.array([1,2,4,6])
ar2 = np.array([2.5,8.1,5.63,6.66])
print(np.std(ar1))


# Advanced Array Operations

# 41. Index of the maximum value in an array.
ar2 = np.array([2.5,8.1,5.63,6.66])
print("max value index:", np.argmax(ar2))

# 42. Index of the minimum value in an array.
ar2 = np.array([2.5,8.1,5.63,6.66])
print("min value index:", np.argmin(ar2))

# 43.  Median of the elements in an array.
ar2 = np.array([2.5,8.1,5.63,6.66])
print("median:", np.median(ar2))

# 44. **`np.unique()`**: Find the unique elements of an array.
ar2 = np.array([2.5,8.1,5.63,6.66, 6.66, 1.5])
print("unique element:", np.unique(ar2))

# 45. Sort the elements of an array.
ar2 = np.array([2.5,8.1,5.63,6.66, 6.66, 1.5])
print("sort", np.sort(ar2))

# 46. Get the indices that would sort an array.
ar2 = np.array([2.5,8.1,5.63,6.66, 6.66, 1.5])
print("index to sort:", np.argsort(ar2))

# 47. Limit the values in an array to a given range.
ar2 = np.array([2.5,8.1,5.63,6.66, 6.66, 1.5])
print("val:", np.clip(ar2, 2,4))  # [2.5 4.  4.  4.  4.  2. ]

# 48. Cumulative sum of elements in an array.
ar2 = np.array([2.5,8.1,5.63,6.66, 6.66, 1.5])
print("cumsum:", np.cumsum(ar2))

# 49. **`np.cumprod()`**: Cumulative product of elements in an array.
ar2 = np.array([2.5,8.1,5.63,6.66, 6.66, 1.5])
print("cumprod:", np.cumprod(ar2))

# 50. Compute the inverse of a square matrix.
matrix = np.array(np.mat('1 2; 3 4'))
print(matrix)
print(np.linalg.inv(matrix))

print("Done")

arr = np.arange(1,100,2)

# Create a simple array from 1 to 9
arr = np.arange(1, 10, 1)
print("Original Array:")
print(arr)

# Insert the value 5 at index 4 (between 4 and 5)
arr_inserted = np.insert(arr, 4, 5)
print("\nArray after inserting 5 at index 4:")
print(arr_inserted)

# Delete the value at index 4 (the value 5 we just inserted)
arr_deleted = np.delete(arr_inserted, 4)
print("\nArray after deleting the value at index 4:")
print(arr_deleted)

# Search for an element in the array using np.where()
# Find the index of the value 7
indices_of_7 = np.where(arr == 7)
print("\nIndex of value 7 in the original array:")
print(indices_of_7)

# Find elements that are greater than 5
indices_greater_than_5 = np.where(arr > 5)
print("\nIndices of elements greater than 5:")
print(indices_greater_than_5)

# Check if the value 5 is in the array using np.isin()
is_5_in_array = np.isin(5, arr)
print("\nIs 5 in the array?", is_5_in_array)

# Find the index of the maximum and minimum elements
index_of_max = np.argmax(arr)
index_of_min = np.argmin(arr)
print("\nIndex of maximum value:", index_of_max)
print("Index of minimum value:", index_of_min)
