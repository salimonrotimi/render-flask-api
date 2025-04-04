# Agricultural Loan Eligibility Prediction API

This repository contains a Flask API that serves a machine learning model to predict agricultural loan eligibility. The model analyzes applicant data and determines whether they qualify for a loan based on predefined criteria.

## Features
- RESTful API built using Flask
- Machine learning model for loan eligibility prediction
- Easy deployment and scalability

## Technologies Used
- Python
- Flask
- Scikit-learn
- Pandas, NumPy
- Render (for deployment)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/salimonrotimi/render-flask-api.git
   cd render-flask-api
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Flask API locally:
   ```bash
   python app.py
   ```
2. The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints
### 1. Predict Loan Eligibility Example
- **Endpoint:** `/predictapi`
- **Method:** `POST`
- **Request Body (JSON):**
  ```json
  {
    "gender": "male",
    "married": "No",
    "dependents": 2,
    "education": "graduate",
    "self_employed": "yes",
    "applicantIncome": 3500,
    "coapplicantIncome": 1900,
    "loanAmount": 200,
    "loan_amount_term": 360,
    "credit_history": 1,
    "property_area": "Urban"
  }
  ```
- **Response:**
  ```json
  {
    "outpu": 1
  }
  ```
  
  ```
  1 means Yes (Eligigble), 0 means No (Not eligible)  
  ```

## Deployment on Render
To deploy the API on Render, follow these steps:

1. Push your latest code to GitHub.
2. Go to [Render](https://render.com/) and log in.
3. Click on "New Web Service" and connect your GitHub repository.
4. Choose an appropriate runtime (e.g., Python 3.x).
5. Set the build command:
   ```bash
   pip install -r requirements.txt
   ```
6. Set the start command:
   ```bash
   gunicorn app:app
   ```
7. Click "Deploy" and wait for the process to complete.
8. Once deployed, your API will be accessible at the given Render URL.


## Contact
For any inquiries, feel free to reach out via <a href="https://github.com/salimonrotimi">github.com/salimonrotimi</a>
