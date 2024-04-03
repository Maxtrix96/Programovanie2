import time

# Function to time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Create a list to sort
my_list = [64, 34, 25, 12, 22, 11, 90]

# Number of times to run the algorithm
num_iterations = 1000

# Time the function
total_time = 0
for _ in range(num_iterations):
    start_time = time.time()
    sorted_list = bubble_sort(my_list)
    end_time = time.time()
    total_time += end_time - start_time

# Calculate the average elapsed time
average_time = total_time / num_iterations

# Print the average elapsed time
print("Average elapsed time:", average_time, "seconds")
