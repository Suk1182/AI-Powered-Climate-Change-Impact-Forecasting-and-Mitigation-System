
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_impact_model(X_train, y_train, X_test, y_test):
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')
    return model

if __name__ == "__main__":
    # Load processed data (example)
    X_train, y_train = ...  # Load your training data
    X_test, y_test = ...    # Load your test data
    model = train_impact_model(X_train, y_train, X_test, y_test)
    # Save model
    import joblib
    joblib.dump(model, 'models/impact_assessment_model.pkl')
