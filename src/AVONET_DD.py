import pandas as pd

df_AVONET_IUCN = pd.read_csv("./data/AVONET_IUCN.csv")
df_DD = df_AVONET_IUCN[df_AVONET_IUCN["RL Category"] == "DD"]
with open("./output/DataDeficient_Species.txt", "w") as file:
    file.write("Data Deficient AVONET Species: " + str(len(df_DD)) + "\n" + df_DD["Species1"].to_string() + "\n")