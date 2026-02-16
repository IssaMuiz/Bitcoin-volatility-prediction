""""Module for model evaluation"""

from sklearn.metrics import mean_square_error, root_mean_square_error, r2_score


def evaluate_model(X_val):
  """"""
  
  y_pred = model.predict(X_val)