import matplotlib.pyplot as mplt
import numpy as np

# Task 1
x = np.arange(0, 21)
print(x)

my_mean = np.mean(x)
print("The mean is ", my_mean)

my_std = np.std(x)
print("The standard deviation is ", my_std)

vari = np.var(x)
print("The variance of the marks is  ", vari)

# Task 2 - Histogram
nums = [0.5, 0.7, 1, 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]
x_pos = [i for i, _ in enumerate(nums)]
mplt.hist(x_pos, bins, color='gold')
mplt.xlabel("Amount of Numbers")
mplt.ylabel("Amount of Bins")
mplt.title("Numbers against the bins")
mplt.xticks(x_pos, nums)
mplt.show()
