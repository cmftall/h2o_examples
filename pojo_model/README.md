# H2O Pojo Model

## Export Pojo Model

Run the script to export the model.

```
mkdir ./model/

./export_pojo_example.py
```

## Load Pojo Model

Edit and compile the Java file with the H2O model.

```
javac -cp ./model/h2o-genmodel.jar ./model/GBM_model_python_1546412227221_1.java Server.java

java -cp .:./model/h2o-genmodel.jar:./model/ Server
```
