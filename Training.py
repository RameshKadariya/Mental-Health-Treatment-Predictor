# training.py
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib

def load_and_preprocess_data(filepath):
    """Load and preprocess the survey data."""
    # Load dataset
    train_df = pd.read_csv('Survey.csv')
    
    # Define feature columns and target
    feature_cols = ['Age', 'Gender', 'family_history', 'benefits', 'care_options', 
                   'anonymity', 'leave', 'work_interfere']
    X = train_df[feature_cols]
    y = train_df['treatment']
    
    return X, y

def preprocess_features(X):
    """Preprocess features including encoding categorical variables."""
    # Create a copy to avoid modifying the original
    X_encoded = X.copy()
    
    # Initialize dictionary to store label encoders
    label_encoders = {}
    
    # Encode categorical variables
    for col in X_encoded.columns:
        if X_encoded[col].dtype == 'object':  # Check if column is categorical
            le = LabelEncoder()
            # Fill NaN with 'NaN' before encoding
            X_encoded[col] = le.fit_transform(X_encoded[col].fillna('NaN'))
            label_encoders[col] = le
    
    return X_encoded, label_encoders

def train_model(X, y):
    """Train and return a logistic regression model."""
    # Initialize and train the model
    model = LogisticRegression(random_state=0, max_iter=1000)
    model.fit(X, y)
    return model

def save_model_and_encoders(model, label_encoders, model_path='final_model.joblib'):
    """Save the trained model and label encoders to a file."""
    # Create a dictionary with both model and encoders
    to_save = {
        'model': model,
        'label_encoders': label_encoders
    }
    
    # Save to file
    joblib.dump(to_save, model_path)
    print(f"Model and encoders saved to {model_path}")

def main():
    # File path to the dataset
    data_file = 'Survey.csv'
    
    # Load and preprocess data
    X, y = load_and_preprocess_data(data_file)
    
    # Preprocess features (encode categorical variables)
    X_encoded, label_encoders = preprocess_features(X)
    
    # Train the model
    model = train_model(X_encoded, y)
    
    # Save the model and encoders
    save_model_and_encoders(model, label_encoders)
    
    # Optionally print success message
    print("Model training and saving completed successfully!")

if __name__ == "__main__":
    main()