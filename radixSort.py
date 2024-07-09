import time
import random

# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.


def countingSort(arr, exp1):

	n = len(arr)

	# The output array elements that will have sorted arr
	output = [0] * (n)

	# initialize count array as 0
	count = [0] * (10)

	# Store count of occurrences in count[]
	for i in range(0, n):
		index = arr[i] // exp1
		count[index % 10] += 1

	# Change count[i] so that count[i] now contains actual
	# position of this digit in output array
	for i in range(1, 10):
		count[i] += count[i - 1]

	# Build the output array
	i = n - 1
	while i >= 0:
		index = arr[i] // exp1
		output[count[index % 10] - 1] = arr[i]
		count[index % 10] -= 1
		i -= 1

	# Copying the output array to arr[],
	# so that arr now contains sorted numbers
	i = 0
	for i in range(0, len(arr)):
		arr[i] = output[i]

# Method to do Radix Sort


def radixSort(arr):

	# Find the maximum number to know number of digits
	max1 = max(arr)

	# Do counting sort for every digit. Note that instead
	# of passing digit number, exp is passed. exp is 10^i
	# where i is current digit number
	exp = 1
	while max1 / exp >= 1:
		countingSort(arr, exp)
		exp *= 10



# Gerar um array com 100000 números aleatórios no intervalo de 0 a 999999
arr_large = [random.randint(0, 999999) for _ in range(100000)]
# Driver code
arr = [170, 45, 75, 90, 802, 24, 2, 66]

# Measure time
start_time = time.time()

# Function Call
radixSort(arr_large)

end_time = time.time()

# Print sorted array
for i in range(len(arr_large)):
	print(arr_large[i], end=" ")

# Print execution time
print("\nTempo Radix Sort: %s seconds" % (end_time - start_time))

# This code is contributed by Mohit Kumra
# Edited by Patrick Gallagher
