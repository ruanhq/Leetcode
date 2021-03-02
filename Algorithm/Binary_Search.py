#Binary_Search
#排序
#return the index of that column.
def binary_search(arr, low, high, x):
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, high, x)
	else:
		return -1

#bubble sort: n(best) -> n^2(average) -> n^2(worst)
def bubbleSort(arr):
  n = len(arr)
  arri = arr
  for i in range(n - 1):
    for j in range(0, n - i - 1):
      if arri[j] <= arri[j + 1]:
        arri[j], arri[j + 1] = arri[j + 1], arri[j]
  return arri

arr =[1,2,3,4,5,6,7,8,9,10]
bubbleSort(arr)

#mergesort:
def mergeSort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    mergesort(L)
    mergesort(R)
    i = j = k = 0
    #concatenate them together.
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = R[j]
        j += 1
      k += 1
    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1
    while j < len(R):
      arr[k] = R[j]
      j += 1
      k += 1

def partition(arr, low, high):
  i = (low - 1)
  pivot = arr[high]
  for j in range(low, high):
    if arr[j] <= pivot:
      i = i+1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return (i+1)

def quickSort(arr, low, high):
  if len(arr) == 1:
  	return arr
  if low < high:
  	pi = partition(arr, low, high)
  	quickSort(arr, low, pi-1)
  	quickSort(arr, pi+1, high)

def selectionSort(arr):
  n = len(arr)
  for i in range(n):
    min_indx = i
    for j in range(i + 1, n):
      if arr[min_indx] > arr[j]:
      	min_indx = j
    arr[i], arr[min_indx] = arr[min_indx], arr[i]

#n^2 -> n^2 -> n^2
def selectionSort(arr):
  n = len(arr)
  for i in range(n):
    min_indx = i 
    for j in range(i+1, n):
      if arr[min_indx] > arr[j]:
        min_indx = j
    arr[i], arr[min_indx] = arr[min_indx], arr[i]

#Insertion Sort:
def insertionSort(arr):
  n = len(arr)
  for i in range(1, n):
  	key = arr[i]
  	j = i-1
  	while j >= 0 and key < arr[j]:
  	  arr[j+1]= arr[j]
  	  j -= 1
  	arr[j+1] = key

def insertionSort(arr):
  n = len(arr)
  for i in range(1, n):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key
  return arr

arr = [12, 11, 14, 3, 6, 4, 1, 10]
insertionSort(arr)























