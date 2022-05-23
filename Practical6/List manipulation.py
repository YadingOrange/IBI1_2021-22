import numpy as np
import matplotlib.pyplot as plt
marks = [45, 36, 86, 57, 53, 92, 65, 45]
print(sorted(marks))
# Set some details about the boxplot.
plt.boxplot(marks)
plt.title("marks")
plt.show()
# Then we get a boxplot displaying the distribution of marks.
i = 0
total_marks = 0
number = len(marks)
print(number)
while i < number-1:
    total_marks += marks[i]
    i += 1
average = total_marks/number
print("the average mark is", average)
if average < 60:
    print("Rob has failed his ICA.")
else:
    print("Rob has passed his ICA.")
