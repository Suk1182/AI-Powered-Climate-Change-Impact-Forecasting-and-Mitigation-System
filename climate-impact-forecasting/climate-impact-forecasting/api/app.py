
from flask import Flask, request, jsonify
from endpoints import forecast_climate, assess_impact

app = Flask(__name__)

@app.route('/forecast', methods=['POST'])
def forecast():
    data = request.json
    result = forecast_climate(data)
    return jsonify(result)

@app.route('/assess_impact', methods=['POST'])
def assess():
    data = request.json
    result = assess_impact(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
