
import pandas as pd
import matplotlib.pyplot as plt
# Q6.
# Create a bar chart for subjects and marks:

# Subjects: ['Maths', 'Science', 'English']
Subjects= ['Maths', 'Science', 'English']
Marks= [85, 90, 78]
# Marks: [85, 90, 78]
plt.bar(Subjects,Marks)

plt.title("Student Mark in Bar Chart")

plt.show()