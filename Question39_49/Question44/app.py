from flask import Flask, request, jsonify
import joblib  # For loading the ML model

app = Flask(__name__)

# Load your pre-trained machine learning model
model = joblib.load('model.gz')

@app.route('/predict', method= ['POST'])
def predict():
    # Get the data from the POST request
    data = request.get_json(force=True)
    
    # Assuming the data is a list of features
    prediction = model.predict([data['features']])
    
    # Return the prediction as JSON
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
