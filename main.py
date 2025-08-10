from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import pickle
import numpy as np
import warnings

app = Flask(__name__)

# Load model and data with proper error handling
try:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = pickle.load(open('RidgeModel.pkl', 'rb'))
    print("Model loaded successfully!")
    MODEL_LOADED = True
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    MODEL_LOADED = False

data = pd.read_csv('Cleaned_data.csv')

@app.route('/')
def index():
    # Always return a clean form - no previous data
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations, model_loaded=MODEL_LOADED)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if not MODEL_LOADED:
            return render_template('index.html', 
                                 locations=sorted(data['location'].unique()),
                                 error="Model is not loaded properly.",
                                 model_loaded=MODEL_LOADED)
        
        # Get form data
        location = request.form.get('location', '').strip()
        bhk = request.form.get('bhk', '').strip()
        bath = request.form.get('bath', '').strip()
        total_sqft = request.form.get('total_sqft', '').strip()
        
        print(f"Raw form data: location='{location}', bhk='{bhk}', bath='{bath}', sqft='{total_sqft}'")
        
        # Comprehensive validation
        errors = []
        
        if not location or location == "Choose a location...":
            errors.append("Please select a valid location.")
        
        if not bhk:
            errors.append("Please enter BHK.")
        else:
            try:
                bhk_val = float(bhk)
                if bhk_val <= 0:
                    errors.append("BHK must be greater than 0.")
            except ValueError:
                errors.append("Please enter a valid number for BHK.")
        
        if not bath:
            errors.append("Please enter number of bathrooms.")
        else:
            try:
                bath_val = float(bath)
                if bath_val <= 0:
                    errors.append("Number of bathrooms must be greater than 0.")
            except ValueError:
                errors.append("Please enter a valid number for bathrooms.")
        
        if not total_sqft:
            errors.append("Please enter total square feet.")
        else:
            try:
                sqft_val = float(total_sqft)
                if sqft_val <= 0:
                    errors.append("Square feet must be greater than 0.")
            except ValueError:
                errors.append("Please enter a valid number for square feet.")
        
        # If there are validation errors, show them without prediction
        if errors:
            error_message = " ".join(errors)
            return render_template('index.html', 
                                 locations=sorted(data['location'].unique()),
                                 error=error_message,
                                 selected_location=location if location != "Choose a location..." else "",
                                 selected_bhk=bhk,
                                 selected_bath=bath,
                                 selected_sqft=total_sqft,
                                 model_loaded=MODEL_LOADED)
        
        # Convert to appropriate types (we know they're valid now)
        bhk = float(bhk)
        bath = float(bath)
        total_sqft = float(total_sqft)
        
        # Check if location exists in our data
        available_locations = sorted(data['location'].unique())
        if location not in available_locations:
            return render_template('index.html', 
                                 locations=available_locations,
                                 error=f"Location '{location}' is not available in our database.",
                                 model_loaded=MODEL_LOADED)
        
        print(f"Validated input: location={location}, bhk={bhk}, bath={bath}, sqft={total_sqft}")
        
        # Create input DataFrame for prediction
        input_data = pd.DataFrame({
            'total_sqft': [total_sqft],
            'bath': [bath], 
            'bhk': [bhk],
            'location': [location]
        })
        
        print(f"Input DataFrame:\n{input_data}")
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        prediction = round(abs(prediction), 2)
        
        print(f"Prediction: {prediction}")
        
        # Return result with prediction
        return render_template('index.html', 
                             locations=available_locations,
                             prediction=prediction,
                             selected_location=location,
                             selected_bhk=bhk,
                             selected_bath=bath,
                             selected_sqft=total_sqft,
                             model_loaded=MODEL_LOADED,
                             show_clear_button=True)  # Add clear button when prediction is shown
    
    except Exception as e:
        print(f"Error in prediction: {e}")
        return render_template('index.html', 
                             locations=sorted(data['location'].unique()),
                             error=f"Prediction error: {str(e)}",
                             model_loaded=MODEL_LOADED)

@app.route('/clear')
def clear_form():
    """Route to clear the form and start fresh"""
    return redirect(url_for('index'))

if __name__ == '__main__':
    print("Starting Flask application...")
    print(f"Data columns: {data.columns.tolist()}")
    print(f"Model loaded: {MODEL_LOADED}")
    print(f"Available locations: {len(sorted(data['location'].unique()))}")
    app.run(debug=True, port=5000)