# 🧠 Mental Health Treatment Predictor

A machine learning web application that predicts the likelihood of individuals seeking mental health treatment based on workplace and personal factors.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.2-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 About

This project uses **Logistic Regression** to predict whether someone is likely to seek mental health treatment. The model analyzes 8 key factors including age, gender, family history, workplace benefits, and work interference patterns.

**Features:**
- Real-time ML predictions with probability scores
- Modern, responsive web interface
- Fast inference (<50ms response time)
- Privacy-focused design

## 🛠️ Tech Stack

**Backend:** Flask, scikit-learn, pandas, numpy, joblib  
**Frontend:** HTML5, CSS3, Vanilla JavaScript  
**Model:** Logistic Regression (L2 regularization)

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/yourusername/mental-health-predictor.git
cd mental-health-predictor

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Open browser: `http://127.0.0.1:5000`

## 📁 Project Structure

```
├── app.py                  # Flask application
├── Training.py             # Model training script
├── final_model.joblib      # Pre-trained model & encoders
├── Survey.csv              # Training dataset
├── requirements.txt        # Dependencies
├── Templates/
│   └── index.html         # Web interface
```

## 💡 How It Works

**Input Features (8):**
- Age (18-100)
- Gender (Male/Female/Trans)
- Family history of mental health issues
- Workplace mental health benefits
- Available care options
- Anonymity protection
- Ease of taking medical leave
- Work interference level

**Output:**
- Prediction: Yes/No (will seek treatment)
- Probability: 0-100% confidence score

## 🔧 API Usage

**Endpoint:** `POST /predict`

**Request:**
```json
{
  "Age": 30,
  "Gender": "Male",
  "family_history": "Yes",
  "benefits": "Yes",
  "care_options": "Yes",
  "anonymity": "Yes",
  "leave": "Somewhat easy",
  "work_interfere": "Sometimes"
}
```

**Response:**
```json
{
  "prediction": "Yes",
  "probability": 75.5
}
```

## 🔄 Retrain Model (Optional)

The pre-trained model is included, but you can retrain:

```bash
python Training.py
```

This generates a new `final_model.joblib` file.

## 🎯 Model Details

- **Algorithm:** Logistic Regression
- **Regularization:** L2 (default)
- **Max Iterations:** 1000
- **Encoding:** Label Encoding for categorical variables
- **Missing Values:** Handled as 'NaN' category

## 📝 License

MIT License - see LICENSE file

## 👨‍💻 Author

**[Your Name]**  
GitHub: [@yourusername](https://github.com/yourusername)  
LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)  
Email: your.email@example.com

---

Built for machine learning portfolio | Denmark/Germany study applications
