# Introduction to sorting methods
# Deviating from the guide for demonstration purposes
import random

def menu():
    print("1.   Bubble Sort")
    print("2.   Selection Sort")
    print("3.   Insertion Sort")
    print("4.   Merge Sort")
    print("5.   Quick Sort")
    print("0.   EXIT")
    return input()

def bubbleSort():
    # Bubble Sort O(n^2) average & worst, O(n) best
    # Compares & swaps adjacent elements
    compare_count = 0
    swap_count = 0
    for x in range(length):
        for e in range(0, length - x - 1):
            if rand_list[e] > rand_list[e+1]:
                rand_list[e+1], rand_list[e] = rand_list[e], rand_list[e+1]
                swap_count += 1
            compare_count += 1
    print(rand_list)
    print(compare_count)
    print(swap_count)

def selectionSort():
    # More efficient than bubble, O(n^2) for average, worst, and best cases
    # Finds MIN element and moves to 1st position, then grabs next MIN element
    compare_count = 0
    swap_count = 0
    for x in range(length):
        min_index = x
        for e in range(x+1, length):
            if rand_list[e] < rand_list[min_index]:
                min_index = e
                swap_count += 1
            compare_count += 1
        rand_list[min_index], rand_list[x] = rand_list[x], rand_list[min_index]
    print(rand_list)
    print(compare_count)
    print(swap_count)

def insertionSort():
    # Time complexity O(n^2) for average, worst, O(n) for best case
    # Moves elements from unsorted array to newly ALWAYS sorted array
    # More efficient than select or bubble in practice
    compare_count = 0
    # No swaps occurring, elements are being inserted into sorted array
    for x in range(length):
        a = rand_list[x]
        y = x - 1
        while y >= 0 and a < rand_list[y]:
            rand_list[y+1] = rand_list[y]
            y -= 1
            compare_count += 1
        rand_list[y+1] = a
    print(rand_list)
    print(compare_count)

def mergeSort(rand_list):
    # Time Complexity O(nlogn) for worst, average, & best case
    # Array keeps dividing in half, then combined in sorted manner at end
    # Slower than other sorting algorithms for smaller tasks
    # For refresher: https://www.youtube.com/watch?v=cVZMah9kEjI
    if len(rand_list) > 1:
        left_array = rand_list[:len(rand_list)//2]
        right_array = rand_list[len(rand_list)//2:]
        mergeSort(left_array)
        mergeSort(right_array)

        i = j = k = 0
        while i < len(left_array) and k < len(right_array):
            if left_array[i] < right_array[j]:
                rand_list[k] = left_array[i]
                i += 1
            else:
                rand_list[k] = right_array[j]
                j += 1
            k += 1
        while i < len(left_array):
            rand_list[k] = left_array[i]
            i += 1
            k += 1
        while k < len(right_array):
            rand_list[k] = right_array[j]
            j += 1
            k += 1

def quickSort_partition(rand_list, low, high):
    # Time Complexity O(nlogn) for average & best, O(n^2) for worst case
    # In practice however, faster than merge sort
    # Also a divide & conquer based algorithm like merge sort
    # For refresher: https://www.youtube.com/watch?v=9KBwdDEwal8
    pivot = rand_list[high]
    i = low - 1
    for j in range(low, high):
        if rand_list[j] <= pivot:
            i = i+1
            rand_list[i], rand_list[j] = rand_list[j], rand_list[i]
    rand_list[i+1], rand_list[high] = rand_list[high], rand_list[i+1]
    return i + 1

def quickSort(rand_list, low, high):
    if low < high:
        pi = quickSort_partition(rand_list, low, high)
        quickSort(rand_list, low, pi - 1)
        quickSort(rand_list, pi + 1, high)

rand_list = []
# Generate random list within given parameters
# We can also use random.sample(range(0,106), 25)
for x in range(0, 25):
    n = random.randint(0, 106)
    rand_list.append(n)
length = len(rand_list)

userChoice = menu()
if int(userChoice) == 1:
    bubbleSort()
elif int(userChoice) == 2:
    selectionSort()
elif int(userChoice) == 3:
    insertionSort()
elif int(userChoice) == 4:
    mergeSort(rand_list)
    print(rand_list)
elif int(userChoice) == 5:
    quickSort(rand_list, 0, len(rand_list) - 1)
    print(rand_list)
elif int(userChoice) == 0:
    raise SystemExit
else:
    print("Invalid Input.")
    exit(1)
