import pandas as pd
from pandas.core.nanops import F
import matplotlib.pyplot as plt

#AVONET analysis
df = pd.read_csv("data/AVONET.csv")

#Kipps Distance
kipps_distance = df["Kipps.Distance"]
with open("Kipps_distance_comparison.txt", "a") as file:
    file.write("Average Kipp's Distance of Living Birds: " + str(kipps_distance.mean()) + " mm" + "\n")

#Mass
mass = df["Mass"]
with open("Mass_comparison.txt", "a") as file:
    file.write("Average Mass of Living Birds: " + str(mass.mean()) + " g" + "\n")

#Culmen Length
culmen = df["Beak.Length_Culmen"]
with open("Culmen_length_comparison.txt", "a") as file:
    file.write("Average Culmen Length of Living Birds: " + str(culmen.mean()) + " mm" + "\n")

#HWI
hand_wing_index = df["Hand-Wing.Index"]
with open("HWI_comparison.txt", "a") as file:
    file.write("Average Hand Wing Index of Living Birds: " + str(hand_wing_index.mean()) + "\n")

#Order counts and proportions
order_counts = df["Order1"].value_counts()
order_proportions_AVONET = df["Order1"].value_counts(normalize=True)
with open("Order_counts_AVONET.txt", "a") as file:
    file.write("Order counts of Living Birds: " + str(order_counts) + "\n")
    file.write("Order proportions of Living Birds: " + str(order_proportions_AVONET) + "\n")

plt.bar(order_proportions_AVONET.index, order_proportions_AVONET.values)
plt.xlabel("Order")
plt.ylabel("Proportion")
plt.title("Order Proportions of Living Birds")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()






