import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset: CSV with columns ['batch', 'is_biased'] and bit patterns
df = pd.read_csv('data/training_data.csv')
X = df['batch'].apply(lambda s: [int(b) for b in s]).tolist()
y = df['is_biased']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))
joblib.dump(model, 'model.pkl')
