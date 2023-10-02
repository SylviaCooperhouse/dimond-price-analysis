from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict_price():
    try:
        # Get data from the request
        data = request.get_json()
        new_diamond = pd.DataFrame([data])

        # Use the trained model to predict the price
        predicted_price = model.predict(new_diamond)

        # Return the prediction as JSON
        return jsonify({'predicted_price': predicted_price[0]})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)