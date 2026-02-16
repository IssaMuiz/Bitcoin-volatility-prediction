""""Module for model evaluation"""

from sklearn.metrics import mean_squared_error, root_mean_squared_error, r2_score


def evaluate_model(model, X_val, y_val):
    """"""

    y_pred = model.predict(X_val)

    evaluation_report = {
        "MSE" = mean_squared_error(y_pred, y_val),
        "RMSE" = root_mean_squared_error(y_pred, y_val),
        "r2_score" = r2_score(y_pred, y_val)
    }
