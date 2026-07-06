import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/AVOTREX.csv")

#Order counts and proportions
order_counts = df["order"].value_counts()
order_proportions_AVOTREX = df["order"].value_counts(normalize=True)

#Flight ability counts
flight_ability_counts = df["flight_ability"].value_counts()
print(flight_ability_counts)

plt.bar(order_proportions_AVOTREX.index, order_proportions_AVOTREX.values)
plt.xlabel("Order")
plt.ylabel("Proportion")
plt.title("Order Proportions of Extinct Birds")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

plt.bar(flight_ability_counts.index.astype(str), flight_ability_counts.values, width=0.4)
plt.xlabel("Flight Ability")
plt.ylabel("Number of Species")
plt.title("Flight Ability of Extinct Birds")
plt.tight_layout()
plt.show()