import requests

# Define the data to send in the POST request
data = {
    'carat': 1.0,              # Example carat value
    'cut_encoded': 5,          # Example cut_encoded value (e.g., 'Ideal' mapped to 5)
    'color_encoded': 6,        # Example color_encoded value (e.g., 'E' mapped to 6)
    'clarity_encoded': 5,      # Example clarity_encoded value (e.g., 'VS1' mapped to 5)
    'x': 6.5,                  # Example x dimension in mm
    'y': 6.5,                  # Example y dimension in mm
    'z': 4.0,                  # Example z dimension in mm
    'depth': 61.5              # Example depth percentage
}

# Make a POST request to the /predict endpoint
url = "http://127.0.0.1:5000/predict"
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=data, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Print the HTML content received from the Flask app
    print(response.text)
else:
    print("Error:", response.status_code)