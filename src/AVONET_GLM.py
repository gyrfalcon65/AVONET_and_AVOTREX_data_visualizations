import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

#Process and fit the data
df = pd.read_csv("./data/AVONET_IUCN.csv") #Read the AVONET_IUCN csv file
model = smf.glm(formula="np.log(Q('Range.Size')) ~ Q('Hand-Wing.Index') + np.log(Q('Mass'))", data=df, family=sm.families.Gaussian()) #Use HWI and mass as predictors and range size as the response (log-transformed because range size and mass are skewed)
results = model.fit() #Fit the model
print(results.summary()) #Prints the summary of the model

#Plot the data and model
hwi_ordered = np.linspace(df['Hand-Wing.Index'].min(), df['Hand-Wing.Index'].max(), 200) #Creates an array of 200 values between the minimum and maximum HWI
pred_hwi = pd.DataFrame({'Hand-Wing.Index': hwi_ordered, 'Mass': df['Mass'].mean()}) #Creates a dataframe with the HWI values and the mean mass
pred_range1 = np.exp(results.predict(pred_hwi)) #Predicts the range size using the model
plt.scatter(df['Hand-Wing.Index'], df['Range.Size']) #Plots the data points
plt.plot(hwi_ordered, pred_range1, color='red') #Plots the regression line
plt.xlabel('Hand-Wing Index')
plt.ylabel('Range Size (km^2)')
plt.yscale('log')
plt.title('Range Size vs Hand-Wing Index')
plt.savefig("./output/AVONET_GLM_RangeSize_vs_HWI.png", dpi=300, bbox_inches="tight")
plt.show()

mass_ordered = np.linspace(df['Mass'].min(), df['Mass'].max(), 200) #Creates an array of 200 values between the minimum and maximum mass so we connect the data points in order from least to greatest
pred_mass = pd.DataFrame({'Mass': mass_ordered, 'Hand-Wing.Index': df['Hand-Wing.Index'].mean()}) #Creates a dataframe with the mass values and the mean HWI
pred_range2 = np.exp(results.predict(pred_mass)) #Predicts the range size using the model, used to plot the regression curve/line
plt.scatter(df['Mass'], df['Range.Size']) #Plots the data points
plt.plot(mass_ordered, pred_range2, color='red') #Plots the regression line
plt.xlabel('Mass (g)')
plt.ylabel('Range Size (km^2)')
plt.yscale('log')
plt.ylim(0.1, 10**9)
plt.xscale('log')
plt.title('Range Size vs Mass')
plt.savefig("./output/AVONET_GLM_RangeSize_vs_Mass.png", dpi=300, bbox_inches="tight")
plt.show()
