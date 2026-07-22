import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

df_AVONET_IUCN = pd.read_csv("./data/AVONET_IUCN.csv") #Reads in the AVONET_IUCN spreadsheet
df = df_AVONET_IUCN.drop(columns=["Total.individuals", "Complete.measures", "Sequence", "Female", "Male", "Unknown", "Max.Latitude", "Min.Latitude", "Centroid.Longitude", "Centroid.Latitude", "Habitat.Density", "Migration"]).select_dtypes(include=[np.number]).dropna() #Selects the columns with only numbers and removes the rows with missing values
IUCN_categories = df_AVONET_IUCN.loc[df.index, "RL Category"] #Gets the IUCN categories from the AVONET_IUCN spreadsheet
scaler = StandardScaler() #Standardizes the data
scaler.fit(df) #Fits the scaler to the data
scaled_data = scaler.transform(df) #Transforms the data to the standardized space

pca = PCA(n_components=11) #Creates a PCA object with 11 principal components
pca.fit(scaled_data) #Fits the PCA model to the scaled data
x_pca = pca.transform(scaled_data) #Transforms the data to the PCA space

pc_values = np.arange(pca.n_components_)+1 #Creates an array of the principal components
plt.plot(pc_values, pca.explained_variance_ratio_, 'o-', linewidth=2, color='blue') #Plots the scree plot
plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Proportion of Variance Explained')
plt.xticks(np.arange(1, 12, 1)) #Sets the x-axis ticks so that it starts at 1, ends at 11, and increments by 1
plt.savefig("./output/AVONET_PCA_Scree_Plot.png", dpi=300, bbox_inches="tight") #Saves the scree plot to a file with a resolution of 300 dpi and a tight bounding box
# plt.show()

#Plot only the first two principal components because they explain the most variance
plt.figure(figsize=(8, 6)) #Creates a figure with a width of 8 inches and a height of 6 inches
sns.scatterplot(x=x_pca[:, 0], y=x_pca[:, 1], hue=IUCN_categories, hue_order=["LC","NT", "VU", "EN", "CR", "EW", "EX"], palette="viridis") #Plots the PCA scatter plot
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.ylim(-8.5, 11)
plt.xlim(-3, 27)
plt.title("AVONET PCA")
plt.savefig("./output/AVONET_PCA.png", dpi=300, bbox_inches="tight")
# plt.show()

df_comp = pd.DataFrame(pca.components_,columns=df.columns,index=["PC1","PC2", "PC3", "PC4", "PC5", "PC6", "PC7", "PC8", "PC9", "PC10", "PC11"]) #Creates a dataframe of all 11 PCA components
plt.figure(figsize=(16, 10))
sns.heatmap(df_comp, annot=True, cmap="plasma") #Plots the PCA components heatmap
plt.title("AVONET PCA Components Heatmap")
plt.savefig("./output/AVONET_PCA_Components_Heatmap.png", dpi=300, bbox_inches="tight")
# plt.show()

#Plot the PCA again but without the LC category
plt.figure(figsize=(8, 6))
not_lc = IUCN_categories != "LC" #Creates a boolean array of the rows that are not LC
sns.scatterplot(x=x_pca[not_lc, 0], y=x_pca[not_lc, 1], hue=IUCN_categories[not_lc], hue_order=["NT", "VU", "EN", "CR", "EW", "EX"], palette="viridis") #Plots the PCA scatter plot without the LC category
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.ylim(-8, 11)
plt.xlim(-3, 27)
plt.title("AVONET PCA without LC Dots")
plt.savefig("./output/AVONET_PCA_without_LC.png", dpi=300, bbox_inches="tight")
# plt.show()

#Get the PC values for each species in AVONET
df_PCA = pd.DataFrame(x_pca, columns=["PC1", "PC2", "PC3", "PC4", "PC5", "PC6", "PC7", "PC8", "PC9", "PC10", "PC11"], index=df.index)
merged_df = pd.merge(df_AVONET_IUCN, df_PCA, left_index=True, right_index=True)
merged_df.to_csv("./data/AVONET_IUCN_PCA_values.csv")

#Make a 3D scatter plot of the PCA
fig = px.scatter_3d(merged_df, x="PC1", y="PC2", z="PC3", color="RL Category", color_discrete_sequence=px.colors.qualitative.Prism, hover_name="Species1")
fig.update_traces(marker=dict(size=2))#Make the dots smaller
fig.update_layout(title="AVONET PCA 3D Plot")
fig.write_image("./output/AVONET_PCA_3D_Plot.png", width=2000, height=2000)
fig.write_html("./output/AVONET_PCA_3D_Plot.html")
#fig.show()

plt.figure(figsize=(10, 10), facecolor="white")
plt.hexbin(merged_df["PC1"], merged_df["PC2"], gridsize=400, cmap = "viridis")
plt.xlim(-2.3, 4)
plt.ylim(-3, 3)
plt.title("AVONET PCA Hexbin Plot")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.savefig("./output/AVONET_PCA_Hexbin_Plot.png", dpi=300, bbox_inches="tight")
plt.show()