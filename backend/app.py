from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Load model from file
model = joblib.load('sonar_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)

    prediction = model.predict(features)[0]

    # Automatic label handling
    if prediction in ['M', 1]:
        result = "Mine"
    else:
        result = "Rock"

    return jsonify({'prediction': result})
if __name__ == '__main__':
    app.run(debug=True)