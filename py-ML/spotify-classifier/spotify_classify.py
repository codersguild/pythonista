# Choose packages to do ML.
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Read the CSV File
spotify_data = pd.read_csv("genre_detect.csv")

# Input Split Data
input_X = spotify_data.drop(columns=['genre'])

# Output Split Data
output_Y = spotify_data['genre']

# Split into training and Test data sets
X_training, X_test, Y_training, Y_test = train_test_split(
    input_X, output_Y, test_size=0.85)

# Choose a machine learning model
ml_model = DecisionTreeClassifier()

# Train and Predict.
ml_model.fit(X_training, Y_training)
predictions = ml_model.predict([[35, 1]])
