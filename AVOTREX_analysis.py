import pandas as pd
from pandas.core.nanops import F
import matplotlib.pyplot as plt

#AVOTREX analysis
df = pd.read_csv("data/AVOTREX.csv")

#Kipps Distance
kipps_distance = df["kipps_distance"]
with open("Kipps_distance_comparison.txt", "a") as file:
    file.write("Average Kipp's Distance of Extinct Birds: " + str(kipps_distance.mean()) + " mm" + "\n")

#Mass
mass = df["body_mass"]
with open("Mass_comparison.txt", "a") as file:
    file.write("Average Mass of Extinct Birds: " + str(mass.mean()) + " g" + "\n")

#Culmen length
culmen_length = df["beak_length_culmen"]
with open("Culmen_length_comparison.txt", "a") as file:
    file.write("Average Culmen Length of Extinct Birds: " + str(culmen_length.mean()) + " mm" + "\n")

#Hand-Wing Index
hand_wing_index = (df["kipps_distance"]/df["wing_length"] * 100)
with open("HWI_comparison.txt", "a") as file:
    file.write("Average Hand-Wing Index of Extinct Birds: " + str(hand_wing_index.mean()) + "\n")

#Order counts and proportions
order_counts = df["order"].value_counts()
order_proportions_AVOTREX = df["order"].value_counts(normalize=True)
with open("Order_counts_AVOTREX.txt", "a") as file:
    file.write("Order counts of Extinct Birds: " + str(order_counts) + "\n")
    file.write("Order proportions of Extinct Birds: " + str(order_proportions_AVOTREX) + "\n")

plt.bar(order_proportions_AVOTREX.index, order_proportions_AVOTREX.values)
plt.xlabel("Order")
plt.ylabel("Proportion")
plt.title("Order Proportions of Extinct Birds")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()