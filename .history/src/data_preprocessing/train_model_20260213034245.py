"""First model training"""

from sklearn.linear_model import LinearRegression


def train_model(X_train, y_train):
    """

    """
    model = LinearRegression()
    model.fit(X_train, y_train)

    return model

def run_model (X_train, y_train, X_val, y_val):
    