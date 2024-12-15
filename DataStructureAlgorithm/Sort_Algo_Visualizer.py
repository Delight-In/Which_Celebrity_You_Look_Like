# Bubble Sort
# Selection Sort
# Insertion Sort
# Merge Sort
# Quick Sort
# Heap Sort
# Radix Sort
# Counting Sort
# Bucket Sort

import matplotlib.pyplot as plt
import numpy as np
import random
import time

# Function to perform Bubble Sort and visualize each step
def bubble_sort_visualized(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='skyblue')

    def update_bars():
        for i, bar in enumerate(bars):
            bar.set_height(arr[i])
        plt.pause(0.1)  # Pause to allow the plot to update

    # Bubble Sort with visualization
    for i in range(n):
        for j in range(0, n-i-1):
            # Highlight the pair being compared
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap elements
            # Update the bar heights
            update_bars()
        time.sleep(0.2)  # Slow down the animation for better visualization

    plt.show()

# Generate a random list of integers
arr = random.sample(range(1, 30), 15)

# Call the function to visualize Bubble Sort
bubble_sort_visualized(arr)




import matplotlib.pyplot as plt
import numpy as np
import random
import time

# Selection Sort with visualization
def selection_sort_visualized(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='skyblue')

    def update_bars():
        for i, bar in enumerate(bars):
            bar.set_height(arr[i])
        plt.pause(0.1)  # Pause to allow the plot to update

    # Selection Sort algorithm
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap if needed
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        update_bars()
        time.sleep(0.2)  # Slow down the animation for better visualization

    plt.show()

# Generate a random list of integers
arr = random.sample(range(1, 30), 15)
selection_sort_visualized(arr)




# Insertion Sort with visualization
def insertion_sort_visualized(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='skyblue')

    def update_bars():
        for i, bar in enumerate(bars):
            bar.set_height(arr[i])
        plt.pause(0.1)  # Pause to allow the plot to update

    # Insertion Sort algorithm
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        update_bars()
        time.sleep(0.2)  # Slow down the animation for better visualization

    plt.show()

# Generate a random list of integers
arr = random.sample(range(1, 30), 15)
insertion_sort_visualized(arr)



# Merge Sort with visualization
def merge_sort_visualized(arr):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='skyblue')

    def update_bars():
        for i, bar in enumerate(bars):
            bar.set_height(arr[i])
        plt.pause(0.1)  # Pause to allow the plot to update

    def merge(left, right):
        merged = []
        while left and right:
            if left[0] < right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        merged.extend(left)
        merged.extend(right)
        return merged

    def merge_sort_helper(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            left = merge_sort_helper(left)
            right = merge_sort_helper(right)
            arr[:] = merge(left, right)
            update_bars()
            time.sleep(0.2)  # Slow down the animation for better visualization
        return arr

    merge_sort_helper(arr)
    plt.show()

# Generate a random list of integers
arr = random.sample(range(1, 30), 15)
merge_sort_visualized(arr)




# Quick Sort with visualization
def quick_sort_visualized(arr):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='skyblue')

    def update_bars():
        for i, bar in enumerate(bars):
            bar.set_height(arr[i])
        plt.pause(0.1)  # Pause to allow the plot to update

    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            update_bars()
            time.sleep(0.2)  # Slow down the animation for better visualization
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        update_bars()
        time.sleep(0.2)
        return i + 1

    quick_sort_helper(arr, 0, len(arr) - 1)
    plt.show()

# Generate a random list of integers
arr = random.sample(range(1, 30), 15)
quick_sort_visualized(arr)

