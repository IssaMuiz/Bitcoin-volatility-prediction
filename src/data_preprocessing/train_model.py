"""First model training"""

from sklearn.linear_model import LinearRegression
from src.data_preprocessing.evaluate_model import evaluate_model


def train_model(X_train, y_train):
    """

    """
    model = LinearRegression()
    model.fit(X_train, y_train)

    return model


def run_model(X_train, y_train, X_val, y_val):

    model = train_model(X_train, y_train)

    evaluate = evaluate_model(model, X_val, y_val)

    return evaluate
