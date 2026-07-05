import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/AVOTREX.csv")

#Order counts and proportions
order_counts = df["order"].value_counts()
order_proportions_AVOTREX = df["order"].value_counts(normalize=True)

plt.bar(order_proportions_AVOTREX.index, order_proportions_AVOTREX.values)
plt.xlabel("Order")
plt.ylabel("Proportion")
plt.title("Order Proportions of Extinct Birds")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()