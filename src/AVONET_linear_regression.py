import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from scipy import stats
import matplotlib.pyplot as plt

df_AVONET_IUCN = pd.read_csv("./data/AVONET_IUCN.csv") #Reads in the AVONET_IUCN spreadsheet
x = np.array(df_AVONET_IUCN["Tarsus.Length"]).reshape(-1, 1) #Reshapes the tarsus length data into a 2D array, which is required for sklearn
y = np.array(df_AVONET_IUCN["Wing.Length"]) #Sets the wing length data as the dependent variable - no reshaping needed because the y is allowed to be 1D
x_flat = x.flatten() #Flattens the tarsus length data into a 1D array for scipy, which allows 1D arrays for x and y
result = stats.linregress(x_flat, y) #Performs the linear regression using scipy (needed to get the p-value)
model = LinearRegression().fit(x, y) #Performs the linear regression using sklearn
r_squared = model.score(x, y) #Calculates the coefficient of determination using sklearn
print(f"Coefficient of determination: {r_squared}") #Prints the coefficient of determination
print(f"Intercept: {model.intercept_}") #Prints the intercept
print(f"Slope: {model.coef_}") #Prints the slope
y_pred = model.predict(x) #Predicts the wing length using the model
print(f"Predicted values: {y_pred[:5]}") #Prints the first 5 predicted values
print(f"P-value: {result.pvalue:.2e}") #Prints the p-value (scipy)

#Plot the data points and regression line
plt.scatter(x, y) #Plots the data points
plt.plot(x, y_pred, color="red") #Plots the regression line
plt.xlabel("Tarsus Length (mm)")
plt.ylabel("Wing Length (mm)")
plt.ylim(0, 1000)
plt.title("Linear Regression of Wing Length vs. Tarsus Length")
plt.savefig("./output/AVONET_Wing_Length_vs_Tarsus_Length_Linear_Regression.png", dpi=300, bbox_inches="tight")
plt.show()