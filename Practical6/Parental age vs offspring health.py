# install and import matplotlib
# create two dictionaries showing paternal age and risk of CHD respectively
# plot the relationship between paternal age of risk of CHD


import numpy as np
import matplotlib.pyplot as plt
# The values in the same position in each list correspond to each other.
N = 10
paternal_age = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
chd = [1.03, 1.07, 1.11, 1.17, 1.23, 1.32, 1.42, 1.55, 1.72, 1.94]
print(paternal_age)
print(chd)  # show the dictionary--Task 1
plt.scatter(paternal_age, chd, marker='o')
plt.xlabel("paternal age")
plt.ylabel("Risk of CHD")
# Then we get a scatter plot describing the data--Task 2
plt.show()
p = int(input())
i = 0
while i < 9:
    q = paternal_age[i]
    if p == q:
        print(chd[i])
    i += 1  # Then we find the relative rate of CHD for a given input paternal age.--Task 3
