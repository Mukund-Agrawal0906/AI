import numpy as np

# Create a 2D array (5x6) with random values
array_2d = np.random.randint(0, 10, (5, 6))

# Flatten the array to a 1D array and calculate the frequency using numpy's unique function
unique_values, counts = np.unique(array_2d, return_counts=True)

# Display the results
for value, count in zip(unique_values, counts):
    print(f"The frequency of {value} is {count}")
