import numpy as np
import matplotlib.pyplot as plt
#The values in the same position in each list correspond to each other.
N = 10
paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
plt.scatter(paternal_age,chd,marker='o')
#Then we get a scatter plot describing the data.
