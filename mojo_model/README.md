# H2O Mojo Model

## Export Mojo Model

Run the script to export the model.

```
mkdir ./model/

./export_mojo_example.py
```

## Load Mojo Model

Edit and compile the Java file with the H2O model.

```
javac -cp ./model/h2o-genmodel.jar -J-Xms2g -J-XX:MaxPermSize=128m ./Server.java

java -cp .:./model/h2o-genmodel.jar Server
```
