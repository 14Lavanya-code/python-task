import pandas as pd
import matplotlib.pyplot as plt
# Q10.
# Create a pie chart to represent market share using:

# Values: [40, 30, 20, 10]
Values=[40, 30, 20, 10]
# Companies: ['A', 'B', 'C', 'D']
Companies=['A', 'B', 'C', 'D']
# Use different colors for each slice.
plt.pie(Values,labels=Companies)
plt.show()