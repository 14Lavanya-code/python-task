import pandas as pd
import matplotlib.pyplot as plt
# Draw a line chart for daily temperatures using the data
print("line chart for daily temperatures using the data")
# Temperatures: [28, 30, 32, 31, 29]
temp=[28,30,32,31,29]
plt.plot(temp,color="red")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Dailt Temperature  Line Chart")
plt.show()
# Use red color for the line.