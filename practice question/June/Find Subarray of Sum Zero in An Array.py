def subArrayExists(arr, n):

	n_sum = 0
	s = set()

	for i in range(n):
		n_sum += arr[i]

		if n_sum == 0 or n_sum in s:
			return True
		s.add(n_sum)

	return False

# Driver Code

# arr = [-3, 2, 3, 1, 6]
arr = [1, 4, -2, -2, 5, -4, 3]
n = len(arr)
if subArrayExists(arr, n) == True:
	print("Found a subarray with 0")
else:
	print("No such subarray exist")