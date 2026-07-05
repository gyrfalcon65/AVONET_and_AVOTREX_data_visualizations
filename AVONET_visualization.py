import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/AVONET.csv")

#Order counts and proportions
order_counts = df["Order1"].value_counts()
order_proportions_AVONET = df["Order1"].value_counts(normalize=True)

plt.bar(order_proportions_AVONET.index, order_proportions_AVONET.values)
plt.xlabel("Order")
plt.ylabel("Proportion")
plt.title("Order Proportions of Living Birds")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()