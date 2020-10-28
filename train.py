from sklearn import datasets
from sklearn import svm
import joblib
import os

def train(data):
    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(data.data[:-1], data.target[:-1])

    return clf

def load_data():
    return datasets.load_digits()

def save_model(model):
    joblib.dump(model, os.path.join(os.environ["MODEL_PATH"], "saved_model.pkl"))

if __name__ == "__main__":
    print("Loading data...")
    data = load_data()

    print("Training model...")
    model = train(data)

    print("Saving model...")
    save_model(model)

    print("All done!")
