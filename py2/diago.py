import numpy as np

n_array = np.array([[55, 25, 15],
                    [30, 44, 2],
                    [11, 45, 77]])


print("Numpy Matrix is:")
print(n_array)

trace = np.trace(n_array)

print("\nTrace of given 3X3 matrix:")
print(trace)
