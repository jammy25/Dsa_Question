# Time Complexity = O(n^2)
# Space Complexity = O(1)

def subArraySum(arr, n, sum):
	for i in range(n):
		curr_sum = arr[i]

		j = i + 1
		while j <= n:

			if curr_sum == sum:
				print("Sum found between indexes %d and %d" %(i, j - 1))
				
				return 

			if curr_sum > sum or j == n:
				break
			
			curr_sum = curr_sum + arr[j]
			j += 1

	print("No subarray found")
	return 

# Driver Code

arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum = 23
subArraySum(arr, n, sum)