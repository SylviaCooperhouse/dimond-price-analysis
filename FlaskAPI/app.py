from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

# Initialize a variable to store the predicted result
predicted_result = None

@app.route('/predict', methods=['POST'])
def predict_price():
    try:
        global predicted_result  # Use the global variable

        # Get data from the request
        data = request.get_json()
        new_diamond = pd.DataFrame([data])

        # Use the trained model to predict the price
        predicted_price = model.predict(new_diamond)[0]

        # Store the predicted result
        predicted_result = {
            'input_data': data,
            'predicted_price': predicted_price
        }

        return jsonify(predicted_result)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/')
def index():
    if predicted_result:
        # If a prediction has been made, display it
        return render_template('result.html', input_data=predicted_result['input_data'], predicted_price=predicted_result['predicted_price'])
    else:
        # If no prediction has been made, show the welcome message
        return "Welcome to the Diamond Price Prediction API!"

if __name__ == '__main__':
    app.run(debug=True)