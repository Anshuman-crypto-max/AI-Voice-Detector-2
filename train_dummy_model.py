# Improved dummy model: balanced predictions for demo
# This script creates a scikit-learn model that predicts 'AI' and 'Human' equally
# Run this to overwrite voice_model.pkl for backend testing

import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

# Generate dummy MFCC-like features (e.g., 13 per sample)
X = np.random.rand(40, 13)
# Balanced targets: 20 'AI', 20 'Human'
y = np.array([0]*20 + [1]*20)

# Shuffle the data to avoid order bias
idx = np.random.permutation(len(y))
X, y = X[idx], y[idx]

# Train a simple classifier
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X, y)

# Add class labels for compatibility with backend
clf.classes_ = np.array(['AI', 'Human'])

# Save the model
joblib.dump(clf, 'voice_model.pkl')
print('Balanced dummy model saved as voice_model.pkl')
