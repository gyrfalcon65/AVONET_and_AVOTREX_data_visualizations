import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df_AVONET_IUCN = pd.read_csv("./data/AVONET_IUCN.csv") #Reads in the AVONET_IUCN spreadsheet
df = df_AVONET_IUCN.drop(columns=["Total.individuals", "Female", "Male", "Unknown", "Max.Latitude", "Min.Latitude", "Centroid.Longitude", "Centroid.Latitude", "Range.Size"]).select_dtypes(include=[np.number]).dropna() #Selects the columns with only numbers and removes the rows with missing values
IUCN_categories = df_AVONET_IUCN.loc[df.index, "RL Category"]
scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)

pca = PCA(n_components=2)
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=x_pca[:, 0], y=x_pca[:, 1], hue=IUCN_categories, hue_order=["LC", "NT", "VU", "EN", "CR", "EW", "EX"], palette="viridis")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.ylim(-8, 6)
plt.xlim(-3, 27)
plt.title("AVONET PCA")
plt.savefig("./output/AVONET_PCA.png", dpi=300, bbox_inches="tight")
plt.show()

df_comp = pd.DataFrame(pca.components_,columns=df.columns,index=["PC1","PC2"])
plt.figure(figsize=(16, 10))
sns.heatmap(df_comp, annot=True, cmap="viridis")
plt.title("AVONET PCA Components Heatmap")
plt.show()
plt.savefig("./output/AVONET_PCA_Components.png", dpi=300, bbox_inches="tight")
