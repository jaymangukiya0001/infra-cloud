# infra-cloud
this reposiratory is for the assignment of infracloud technologies.

this repo contains programming about the short the url and it's related unittestcase, server and dockerfile for that.

this assignment has mainly two parts.
1. Flask Server
2. Python file

1. Flask Server 
Flask server is used to call the api of bitly to short the url. The code related to this file is in the Mockserver folder it has api_call endpoint that will be called for shorten the URL. it only accepts the GET request only and path as a argument.
it also contains checkpoint that the url which we pass as an argument is we have already done request or not? if we have done than it will check in the json file if it is present than it will return shorten url which is in the json file. else it will call the bitly api. if something goes wrong than it will return error string containing json obj.

2. Python file.
mock_server_call python file is used to call the server which is created earlier using flask. it is mainly used to take input of url and taking the response from the flask server.


in /test:
in a test folder test_api_call.py contains unit test case for that.

Dockerfile and docker-compose.yml 
this files are used to dockerize the app

url_storage.json:
this file is used to store the long_url and it's shorten url as a key-value pair in a json format
json file in a Mockserver folder is storing the details. while the json file which is outside that is used for the unitesting.

requirements.txt:
this file contains the required libraries for the running app in the docker.

to run the unittest in docker use below command from infra-cloud directory:
docker-compose up

to run the flask server in docker use below commands from infra-cloud directory.
1. docker image build -t flask_docker .
2. docker run -p 5000:5000 -d flask_docker
then use docker terminal to intract with app using docker desktop.