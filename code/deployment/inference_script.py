import argparse
import os
from azureml.core import Run, Model, Workspace
from sklearn.externals import joblib

run = Run.get_context()

test_dataset = run.input_datasets['input1']

model_path = Model.get_model_path("livedoor-model")
print("model path : ", model_path)

model = joblib.load(model_path)

predicted = model.predict_proba(test_dataset.take(1).to_pandas_dataframe())
print(predicted)