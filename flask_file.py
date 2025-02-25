import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load dataset
df = pd.read_csv("new_loan_application_data.csv")

# Preprocess data
df.drop(columns=['applicant_id'], inplace=True)  # Remove unnecessary column

# Split dataset
X = df.drop(columns=['loan_status'])
y = df['loan_status'].map({'Approved': 1, 'Rejected': 0})
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    input_data = pd.DataFrame([data])
    prediction = model.predict(input_data)[0]  # Replace with trained model
    result = "Approved" if prediction == 1 else "Rejected"
    return jsonify({"loan_status": result})

if __name__ == "__main__":
    app.run(debug=True)
