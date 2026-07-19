import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df_AVONET_IUCN = pd.read_csv("./data/AVONET_IUCN.csv") #Reads in the AVONET_IUCN spreadsheet
df = df_AVONET_IUCN.drop(columns=["Total.individuals", "Complete.measures", "Sequence", "Female", "Male", "Unknown", "Max.Latitude", "Min.Latitude", "Centroid.Longitude", "Centroid.Latitude", "Habitat.Density", "Migration"]).select_dtypes(include=[np.number]).dropna() #Selects the columns with only numbers and removes the rows with missing values
IUCN_categories = df_AVONET_IUCN.loc[df.index, "RL Category"] #Gets the IUCN categories from the AVONET_IUCN spreadsheet
scaler = StandardScaler() #Standardizes the data
scaler.fit(df) #Fits the scaler to the data
scaled_data = scaler.transform(df)

pca = PCA(n_components=11)
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)

pc_values = np.arange(pca.n_components_)+1
plt.plot(pc_values, pca.explained_variance_ratio_, 'o-', linewidth=2, color='blue')
plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Proportion of Variance Explained')
plt.xticks(np.arange(1, 12, 1))
plt.savefig("./output/AVONET_PCA_Scree_Plot.png", dpi=300, bbox_inches="tight")
plt.show()

#Plot only the first two principal components because they explain the most variance
plt.figure(figsize=(8, 6))
sns.scatterplot(x=x_pca[:, 0], y=x_pca[:, 1], hue=IUCN_categories, hue_order=["LC","NT", "VU", "EN", "CR", "EW", "EX"], palette="viridis")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.ylim(-8, 11)
plt.xlim(-3, 27)
plt.title("AVONET PCA")
plt.savefig("./output/AVONET_PCA.png", dpi=300, bbox_inches="tight")
plt.show()

df_comp = pd.DataFrame(pca.components_,columns=df.columns,index=["PC1","PC2", "PC3", "PC4", "PC5", "PC6", "PC7", "PC8", "PC9", "PC10", "PC11"])
plt.figure(figsize=(16, 10))
sns.heatmap(df_comp, annot=True, cmap="plasma")
plt.title("AVONET PCA Components Heatmap")
plt.savefig("./output/AVONET_PCA_Components.png", dpi=300, bbox_inches="tight")
plt.show()

#Plot the PCA again but without the LC category
plt.figure(figsize=(8, 6))
not_lc = IUCN_categories != "LC"
sns.scatterplot(x=x_pca[not_lc, 0], y=x_pca[not_lc, 1], hue=IUCN_categories[not_lc], hue_order=["NT", "VU", "EN", "CR", "EW", "EX"], palette="viridis")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.ylim(-8, 11)
plt.xlim(-3, 27)
plt.title("AVONET PCA without LC Dots")
plt.savefig("./output/AVONET_PCA_without_LC.png", dpi=300, bbox_inches="tight")
plt.show()
