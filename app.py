# To deploy this on "RENDER"
# 1. Create a vitual environment with "python -m venv virtualEnvName" e.g. projvenv
# 2. Activate the vitual environment with "projvenv\Scripts\activate"
# 3. Install dependencies (flask, numpy, flask_cors, pandas, matplotlib, scikit-learn) with pip
# 4. pip install gunicorn (a package which is used to run the app on RENDER)
# 5. Generate a "requirements.txt" file which will be used by RENDER to install all the dependencies using
#    "pip freeze > requirements.txt". The file will be auto filled with all the required dependencies.
# 6. Use ".gitignore" to ignore the "projvenv" file.
# 7. Upload all the files to "Github" and then from Github to "RENDER".

from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle as pk

app = Flask(__name__)
CORS(app)
model = pk.load(open("trained_prediction_model.pkl", "rb"))

@app.route("/predictapi", methods = ["POST"])
def predictionapi():      
    data = request.get_json(force=True)
    print(data.values)
    datalist = [int(x) for x in data.values()]
    pred_data = [np.array(datalist)]
    prediction = model.predict(pred_data)
    
    output = round(prediction[0])
    return jsonify(output)

@app.route("/", methods = ["GET"])
def indexpath():
    return jsonify("Welcome, dear user!")

if __name__ == "__main__":
    app.run()         # app.run(debug=True) for development mode

