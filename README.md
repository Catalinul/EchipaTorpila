## Flask app

### Run the application 

In order to run the python file, we need first to specify Flask where should find the application.

```commandline
export FLASK_APP=fruits_app
```

As we are running the application locally we need to specify to Flask also that should run it in development mode. 

```commandline
export FLASK_ENV=development
```

To finally run it, we execute the following command 

```commandline
flask run
```

### Test the application

to be continued


### Run the app in a docker container

pipeline.py can be used to build/build/push/deploy/test the application with Docker.
You can use it in the following ways:

```commandline
python pipeline.py BUILD --dockerFilePath=<arg1> --imageName=<arg2> --imageTag=<arg3>
```

```commandline
python pipeline.py DEPLOY --flavour=[docker/kubernetes] --imageName=<arg2> --imageTag=<arg3>
```

```commandline
python pipeline.py PUSH --containerRegistryUsername=<arg1> --imageName=<arg2> --imageTag=<arg3>
```

```commandline
python pipeline.py TEST --endpoint=<URL>
```
