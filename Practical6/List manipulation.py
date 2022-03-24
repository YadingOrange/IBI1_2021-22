import numpy as np
import matplotlib.pyplot as plt
n = 8
marks = [45,36,86,57,53,92,65,45]
#Set some details about the boxplot.
plt.boxplot(marks,
            vert = False,
            whis = 2,
            patch _artist =True,
            meanline = True,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False
              )
plt.show()
#Then we get a boxplot displaying the distribution of marks.
