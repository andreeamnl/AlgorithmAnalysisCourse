import time
import numpy as np
import matplotlib.pyplot as plt
from time import process_time
import random


#########################################
## Heap Sort #######################
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
  
 # See if left child of root exists and is
 # greater than root
  
    if l < n and arr[i] < arr[l]:
        largest = l
  
 # See if right child of root exists and is
 # greater than root
  
    if r < n and arr[largest] < arr[r]:
        largest = r
  
 # Change root, if needed
  
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
  
  # Heapify the root.
  
        heapify(arr, n, largest)
  
  
# The main function to sort an array of given size
  
def heapSort(arr):
    n = len(arr)
  
 # Build a maxheap.
 # Since last parent will be at ((n//2)-1) we can start at that location.
  
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
  
 # One by one extract elements
  
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)
  


#########################################
## Insertion Sort #######################
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
#########################################

#########################################
## Merge Sort ###########################
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = arr[l + i]

    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr,l,r):
    if l < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = l + (r-l)//2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
#########################################

#########################################
## Quick Sort ###########################
def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low , high):

        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
#########################################



#########################################
## Main #################################

sorts = [
    {
        "name": "Heap Sort",
        "sort": lambda arr: heapSort(arr)
    },
    {
        "name": "Insertion Sort",
        "sort": lambda arr: insertionSort(arr)
    },
    {
        "name": "Merge Sort",
        "sort": lambda arr: mergeSort(arr, 0, len(arr) - 1)
    },
    {
        "name": "Quick Sort",
        "sort": lambda arr: quickSort(arr, 0, len(arr) - 1)
    }
]

elements = np.array([i*1000 for i in range(1, 10)])

plt.xlabel('Input Array of length n')
plt.ylabel('Time Complexity')

for sort in sorts:
    times = list()
    start_all = process_time()
    for i in range(1, 10):
        start = process_time()
        a = random.sample(range(1, 100000), i*1000)
        sort["sort"](a)
        end = process_time()
        times.append(end - start)

        print(sort["name"], "Sorted", i * 1000, "Elements in", end - start, "s")
    end_all = process_time()
    print(sort["name"], "Sorted Elements in", end_all - start_all, "s")

    plt.plot(elements, times, label = sort["name"])

plt.grid()
plt.legend()
plt.show()

#########################################