# -*- coding: utf-8 -*-
"""linear-regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/sksiddique/6e2a3452a78262013fcbb3856dbf6172/linear-regression.ipynb
"""

from sklearn.datasets import fetch_openml

# Fetch the Boston Housing dataset
boston = fetch_openml(name='boston', version=2)

# Convert the data to a Pandas DataFrame
data = pd.DataFrame(boston.data, columns=boston.feature_names)
data['target'] = boston.target

# Display the first few rows of the dataset
print(data.head())

# Optionally, save the dataset to a CSV file
data.to_csv('boston_housing_dataset.csv', index=False)
# Import necessary libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score



oston = load_boston()
data = pd.DataFrame(boston.data, columns=boston.feature_names)
data['target'] = boston.target

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Create a synthetic dataset
np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # Feature
y = 4 + 3 * X + np.random.randn(100, 1)  # Target variable with some noise

# Visualize the data
plt.scatter(X, y)
plt.title("Synthetic Dataset for Linear Regression")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.show()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Visualize the regression line
plt.scatter(X_test, y_test, label="Actual")
plt.plot(X_test, y_pred, color='red', linewidth=3, label="Predicted")
plt.title("Linear Regression Model")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.legend()
plt.show()

