import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

#Process and fit the data
df = pd.read_csv("./data/AVONET_IUCN.csv") #Read the AVONET_IUCN csv file
model = smf.glm(formula="Q('Range.Size') ~ Q('Hand-Wing.Index') + Q('Mass')", data=df, family=sm.families.Gamma(link=sm.families.links.Log())) #Use HWI and mass as predictors and range size as the response
results = model.fit() #Fit the model
print(results.summary())

#Plot the data and model
hwi_ordered = np.linspace(df['Hand-Wing.Index'].min(), df['Hand-Wing.Index'].max(), 200)
pred_hwi = pd.DataFrame({'Hand-Wing.Index': hwi_ordered, 'Mass': df['Mass'].mean()})
pred_range1 = results.predict(pred_hwi)
plt.scatter(df['Hand-Wing.Index'], df['Range.Size'])
plt.plot(hwi_ordered, pred_range1, color='red')
plt.xlabel('Hand-Wing Index')
plt.ylabel('Range Size (km^2)')
plt.yscale('log')
plt.title('Range Size vs Hand-Wing Index')
plt.savefig("./output/AVONET_GLM_RangeSize_vs_HWI.png", dpi=300, bbox_inches="tight")
plt.show()

mass_ordered = np.linspace(df['Mass'].min(), df['Mass'].max(), 200)
pred_mass = pd.DataFrame({'Mass': mass_ordered, 'Hand-Wing.Index': df['Hand-Wing.Index'].mean()})
pred_range2 = results.predict(pred_mass)
plt.scatter(df['Mass'], df['Range.Size'])
plt.plot(mass_ordered, pred_range2, color='red')
plt.xlabel('Mass (g)')
plt.ylabel('Range Size (km^2)')
plt.yscale('log')
plt.ylim(0.1, 10**9)
plt.xscale('log')
plt.title('Range Size vs Mass')
plt.savefig("./output/AVONET_GLM_RangeSize_vs_Mass.png", dpi=300, bbox_inches="tight")
plt.show()
