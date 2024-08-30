
import tensorflow as tf
from tensorflow.keras import layers

def create_model(input_shape):
    model = tf.keras.Sequential([
        layers.LSTM(64, return_sequences=True, input_shape=input_shape),
        layers.LSTM(32),
        layers.Dense(1, activation='linear')
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def train_model(X_train, y_train, X_val, y_val):
    model = create_model((X_train.shape[1], X_train.shape[2]))
    history = model.fit(
        X_train, y_train,
        epochs=50,
        batch_size=32,
        validation_data=(X_val, y_val)
    )
    model.save('models/climate_forecast_model.h5')
    return history

if __name__ == "__main__":
    # Load processed data (example)
    X_train, y_train = ...  # Load your training data
    X_val, y_val = ...      # Load your validation data
    train_model(X_train, y_train, X_val, y_val)
