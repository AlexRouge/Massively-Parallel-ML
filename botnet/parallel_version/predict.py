import numpy as np

def predict(w, b, X):
    # Compute the linear combination of the weights and the example
    z = np.dot(w, X) + b
    # Apply the sigmoid function to get the probability
    p = 1 / (1 + np.exp(-z))
    # Predict the class label (0 or 1) based on the probability
    if p >= 0.5:
        return 1
    else:
        return 0