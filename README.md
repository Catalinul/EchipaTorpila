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

PostMan can be used to test the delete/post/put/get methods on the flask app


### Run the app in a docker container

pipeline.py can be used to build/build/push/deploy/test the application with Docker.
You can use it in the following ways:

Build the image
```commandline
python pipeline.py build --dockerFilePath=<arg1> --imageName=<arg2> --imageTag=<arg3>
```

Push the image on DockerHub
```commandline
python pipeline.py push --containerRegistryUsername=<arg1> --imageName=<arg2> --imageTag=<arg3>
```
Deploy the Flask app using docker
```commandline
python pipeline.py deploy --flavour=docker --imageName=<arg2> --imageTag=<arg3>
```
Deploy the Flask app using kubernetes.
For this step you need to run this command twice, one for the deployment.yaml, one for the service.yaml

```commandline
python pipeline.py deploy --flavour=kubernetes --deploymentManifest=<arg1> --imageName=<arg2> --imageTag=<arg3>
```
Test the endpoint

```commandline
python pipeline.py test --endpoint=<URL>
```
