import pandas as pd
import matplotlib.pyplot as plt

print("Data Visualization") 

# Q1.
# Create a line chart to show student marks using the following data:
print("Create a line chart to show student marks")
# Marks: [50, 60, 70, 80, 90]
Marks=[50,60,70,80,90]
Exam_num=[1,2,3,4,5]
# X-axis: Exam numbers [1, 2, 3, 4, 5]
plt.plot(Exam_num,Marks,marker="o")
plt.xlabel("Exam_number")
plt.ylabel("Marks")
plt.title("Student Mark in Line Chart")

plt.show()

