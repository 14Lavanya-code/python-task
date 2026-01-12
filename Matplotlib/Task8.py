import pandas as pd
import matplotlib.pyplot as plt
# Q8.
# Create a horizontal bar chart for cities and population:
print("Create a horizontal bar chart for cities and population")
# Cities: ['Chennai', 'Madurai', 'Coimbatore']
Cities=['Chennai', 'Madurai', 'Coimbatore']
Population = [10, 5, 7]
# Population (in lakhs): [10, 5, 7]
plt.barh(Cities,Population)

plt.show()