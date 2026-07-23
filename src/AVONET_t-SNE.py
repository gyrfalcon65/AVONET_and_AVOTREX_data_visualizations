import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df_AVONET_IUCN = pd.read_csv("./data/AVONET_IUCN.csv") #Reads in the AVONET_IUCN spreadsheet
df = df_AVONET_IUCN.drop(columns=["Total.individuals", "Complete.measures", "Sequence", "Female", "Male", "Unknown", "Max.Latitude", "Min.Latitude", "Centroid.Longitude", "Centroid.Latitude", "Habitat.Density", "Migration"]).select_dtypes(include=[np.number]).dropna() #Selects the columns with only numbers and removes the rows with missing values
IUCN_categories = df_AVONET_IUCN.loc[df.index, "RL Category"] #Gets the IUCN categories from the AVONET_IUCN spreadsheet
species = df_AVONET_IUCN.loc[df.index, "Species1"] #Gets the species names from the AVONET_IUCN spreadsheet
scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)

model = TSNE(learning_rate=50, random_state=42)
tsne_features = model.fit_transform(scaled_data)

fig = plt.figure(figsize=(10, 10))
sns.scatterplot(x=tsne_features[:,0], y=tsne_features[:,1], hue=IUCN_categories, palette="viridis")
plt.title("t-SNE of AVONET IUCN Data")
plt.xlabel("t-SNE Feature 1")
plt.ylabel("t-SNE Feature 2")
plt.savefig("./output/AVONET_t-SNE.png", dpi=300, bbox_inches="tight")

fig1 = px.scatter(x=tsne_features[:,0], y=tsne_features[:,1], color=IUCN_categories, color_discrete_sequence=px.colors.qualitative.Prism, hover_name=species)
fig1.update_layout(title="t-SNE of AVONET IUCN Data")
fig1.update_xaxes(title="t-SNE Feature 1")
fig1.update_yaxes(title="t-SNE Feature 2")
fig1.write_html("./output/AVONET_t-SNE.html")
fig1.show()

