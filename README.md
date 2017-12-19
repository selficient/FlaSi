# FlaSi webservice
The FlaSi webservice connects the Selficient house to the outside world. It enables users to executes MySQL query's on the local database and interact with HomeLynk domotica objects.

To see the available endpoints please check the live swagger definition that is running after hosting the server.

## Requirements
- Python 3.5.2+
- Connexion


## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```