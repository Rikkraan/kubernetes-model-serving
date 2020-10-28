from sklearn import datasets
from sklearn import svm
from flask import Flask, request, jsonify
import numpy as np
import joblib
import os

APP = Flask(__name__)

def train(data):
    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(data.data[:-1], data.target[:-1])

    return clf

def load_data():
    return datasets.load_digits()

def save_model(model):
    joblib.dump(model, os.path.join(os.environ["MODEL_PATH"], "saved_model.pkl"))

@APP.route("/api/v1/predict", methods=["POST", "GET"])
def predict():
    # breakpoint()
    request_data = request.get_json()
    # data = {"image": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    # 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
    # 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
    # 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,
    # 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
    # 59, 60, 61, 62, 63, 64]}
    model = joblib.load(os.path.join(os.environ["MODEL_PATH"], "saved_model.pkl"))
    prediction = model.predict(np.array(request_data['image']).reshape(1, -1))
    return jsonify({'predicted class is': str(prediction)})


if __name__ == "__main__":
    print("Loading data...")
    data = load_data()

    print("Training model...")
    model = train(data)

    print("Saving model...")
    save_model(model)

    print("All done!")

    print('Starting up API at port 5000')
    APP.run(host='0.0.0.0')
