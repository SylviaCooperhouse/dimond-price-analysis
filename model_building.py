import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib  # Import joblib for model saving

# Load your dataset into a DataFrame (assuming it's already loaded as 'df')
df = pd.read_csv("OneDrive/Documents/2023 Job Applications/diamonds.csv")
df.head()  # Display the first 5 rows

# Encode the 'cut' column into numerical values
cut_mapping = {
    'Fair': 1,
    'Good': 2,
    'Very Good': 3,
    'Premium': 4,
    'Ideal': 5
}
df['cut_encoded'] = df['cut'].map(cut_mapping)

color_mapping = {
    'J': 1,
    'I': 2,
    'H': 3,
    'G': 4,
    'F': 5,
    'E': 6,
    'D': 7
}

# Apply the mapping to the 'color' column
df['color_encoded'] = df['color'].map(color_mapping)

clarity_mapping = {
    'I1': 1,
    'SI2': 2,
    'SI1': 3,
    'VS2': 4,
    'VS1': 5,
    'VVS2': 6,
    'VVS1': 7,
    'IF': 8
}

# Select features and target variable
X = df[['carat', 'cut_encoded', 'color_encoded', 'clarity_encoded', 'x', 'y', 'z', 'depth']]
y = df['price']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest regression model using common n_estimators and random_state to start with
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
# The actual integer value you use for random_state doesn't matter as long as it's consistent across runs for reproducibility.

# Fit the model to the training data
rf_model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(rf_model, 'model.pkl')  # Save the model as 'model.pkl'