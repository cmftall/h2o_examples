#!/usr/bin/env python

import h2o
import json
import pandas as pd


def main():
  h2o.init()

  # Load model
  model_path = "./h2o_model/GLM_model_python_1525320706617_1"
  model = h2o.load_model(model_path)

  with open("data.json", "r") as f:
    json_data_string = json.load(f)

  df = pd.read_json(json_data_string, orient="index")

  test = h2o.H2OFrame(df)

  predictions = model.predict(test)
  predictions.show()

  result_df = predictions.as_data_frame()
  result_string = result_df.to_json(orient='index')
  result = json.loads(result_string)
  print(result)


if __name__ == "__main__":
  main()
