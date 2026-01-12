from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load model and encoders
try:
    model_data = joblib.load('final_model.joblib')
    model = model_data['model']
    label_encoders = model_data['label_encoders']
    app.logger.info("Model and encoders loaded successfully")
except Exception as e:
    app.logger.error(f"Error loading model: {str(e)}")
    raise e

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        app.logger.debug("Received prediction request")
        
        # Get JSON data from frontend
        data = request.get_json()
        app.logger.debug(f"Raw input data: {data}")
        
        # Create DataFrame from input
        input_df = pd.DataFrame([data])
        app.logger.debug(f"Initial DataFrame:\n{input_df}")
        
        # Preprocess input
        for col in input_df.columns:
            if col in label_encoders:
                le = label_encoders[col]
                app.logger.debug(f"Processing column: {col}")
                app.logger.debug(f"Original values: {input_df[col].tolist()}")
                
                # Handle unseen categories
                input_df[col] = input_df[col].apply(
                    lambda x: x if x in le.classes_ else 'NaN'
                )
                app.logger.debug(f"Values after NaN handling: {input_df[col].tolist()}")
                
                input_df[col] = le.transform(input_df[col])
                app.logger.debug(f"Encoded values: {input_df[col].tolist()}")
        
        # Convert age to int
        input_df['Age'] = input_df['Age'].astype(int)
        app.logger.debug(f"DataFrame after preprocessing:\n{input_df}")
        
        # Make prediction
        probability = model.predict_proba(input_df)[0][1]
        prediction = model.predict(input_df)[0]
        app.logger.debug(f"Raw prediction: {prediction}, Probability: {probability}")
        
        # Convert numerical prediction to Yes/No
        result = 'Yes' if prediction == 1 else 'No'
        
        app.logger.info(f"Successful prediction: {result} ({probability:.2%})")
        return jsonify({
            'prediction': result,
            'probability': round(probability * 100, 2)
        })
        
    except Exception as e:
        app.logger.error(f"Prediction error: {str(e)}", exc_info=True)
        return jsonify({
            'error': str(e),
            'message': 'Failed to process prediction'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)