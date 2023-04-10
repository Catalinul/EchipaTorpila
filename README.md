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

#### GET
Create a request for the GET method to fetch all the fruits. Set the URL as http://localhost:5000/fruit/ and set the method to GET.
Create a request for the GET method to fetch a specific fruit by ID. Set the URL as http://localhost:5000/fruit/1 where 1 is the ID of the fruit you want to retrieve. Set the method to GET.

#### POST

Create a request for the POST method to add a new fruit. Set the URL as http://localhost:5000/fruit/ and set the method to POST. Set the body of the request to be a JSON object containing the details of the new fruit.

#### PUT
Create a request for the PUT method to update a fruit by ID. Set the URL as http://localhost:5000/fruit/1 where 1 is the ID of the fruit you want to update. Set the method to PUT. Set the body of the request to be a JSON object containing the updated details of the fruit.

#### DELETE
Create a request for the DELETE method to delete a fruit by ID. Set the URL as http://localhost:5000/fruit/1 where 1 is the ID of the fruit you want to delete. Set the method to DELETE.


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
