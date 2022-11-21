
def bubbleSort(arr):
	n = len(arr)
	swapped = False
	
	for i in range(n):

		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			return
		    
arr = [22,6,7,1,45,0]
bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print( arr[i], end=" ")
