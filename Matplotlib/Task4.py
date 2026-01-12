import matplotlib.pyplot as plt
import pandas as pd

# Q4.
# Create a line chart for runs scored using the data:
print("Create a line chart for runs scored using the data")
# Runs: [45, 60, 75, 90]
Runs= [45, 60, 75, 90]
# Add circle (o) markers to the line.

plt.plot(Runs,marker="s")

plt.title("Runs")
plt.show()