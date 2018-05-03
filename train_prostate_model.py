#!/usr/bin/env python

import h2o
import json


def main():
  h2o.init()

  #df = h2o.import_file(path="smalldata/logreg/prostate.csv")
  prostate = h2o.load_dataset("prostate")
  prostate.describe()

  train, test = prostate.split_frame(ratios=[0.70])
  train["CAPSULE"] = train["CAPSULE"].asfactor()
  test["CAPSULE"] = test["CAPSULE"].asfactor()

  # Train model
  from h2o.estimators import H2OGeneralizedLinearEstimator
  prostate_glm = H2OGeneralizedLinearEstimator(family="binomial", alpha=[0.5])
  prostate_glm.train(
      x=["AGE", "RACE", "PSA", "VOL", "GLEASON"],
      y="CAPSULE",
      training_frame=train)
  prostate_glm.show()

  predictions = prostate_glm.predict(test)
  predictions.show()

  performance = prostate_glm.model_performance(test)
  performance.show()

  # Export model
  model_path = h2o.save_model(prostate_glm, path="./h2o_model", force=True)
  print(model_path)

  model = prostate_glm
  predictions = model.predict(test)
  predictions.show()

  performance = model.model_performance(test)
  performance.show()

  # Export test data
  df = test.as_data_frame()
  with open("data.json", "w") as f:
    #json.dump(df.to_json(orient='records'), f)
    #json.dump(df.to_json(orient='columns'), f)
    json.dump(df.to_json(orient='index'), f)


if __name__ == "__main__":
  main()
