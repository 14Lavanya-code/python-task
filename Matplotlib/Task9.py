import pandas as pd
import matplotlib.pyplot as plt
# Q9.
# Create a pie chart to show time spent in a day using:
# Hours: [8, 6, 4, 6]

# Labels: ['Sleep', 'Work', 'Study', 'Others']
Hours=[8, 6, 4, 6]
Labels= ['Sleep', 'Work', 'Study', 'Others']
plt.pie(Hours,labels=Labels)
plt.show()