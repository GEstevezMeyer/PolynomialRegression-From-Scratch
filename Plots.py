import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Real estate.csv")
plt.scatter(data.X2_house_age, data.Y)
plt.show()