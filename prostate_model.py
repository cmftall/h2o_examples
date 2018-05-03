#!/usr/bin/env python

import h2o


def main():
  h2o.init()
  #df = h2o.import_file(path="smalldata/logreg/prostate.csv") 
  
  prostate = h2o.load_dataset("prostate")
  prostate.describe()

  train, test = prostate.split_frame(ratios=[0.70])
  train["CAPSULE"] = train["CAPSULE"].asfactor()
  test["CAPSULE"] = test["CAPSULE"].asfactor()

  from h2o.estimators import H2OGeneralizedLinearEstimator
  prostate_glm = H2OGeneralizedLinearEstimator(family="binomial", alpha=[0.5])
  prostate_glm.train(x=["AGE", "RACE", "PSA", "VOL", "GLEASON"], y="CAPSULE", training_frame=train)
  prostate_glm.show()
  
  predictions = prostate_glm.predict(test)
  predictions.show()

  performance = prostate_glm.model_performance(test)
  performance.show()


  #import ipdb;ipdb.set_trace()
  model_path = h2o.save_model(prostate_glm, path="./h2o_model", force=True)
  print(model_path)
  saved_model = h2o.load_model(model_path)

  import ipdb;ipdb.set_trace()
  predictions = saved_model.predict(test)
  predictions.show()

  performance = saved_model.model_performance(test)
  performance.show()

if __name__ == "__main__":
  main()
