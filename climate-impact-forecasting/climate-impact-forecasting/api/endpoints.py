
import joblib
import tensorflow as tf

def forecast_climate(data):
    model = tf.keras.models.load_model('models/climate_forecast_model.h5')
    prediction = model.predict(data)
    return {'forecast': prediction.tolist()}

def assess_impact(data):
    model = joblib.load('models/impact_assessment_model.pkl')
    prediction = model.predict(data)
    return {'impact': prediction.tolist()}
