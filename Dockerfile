FROM python:3.8-alpine
# setting working dir
WORKDIR /"infra-cloud"
# adding contents to container
ADD . /"infra-cloud"
# running reuirements.txt
RUN pip3 install -r requirements.txt


RUN chmod a+x run.sh 
ENTRYPOINT [ "python" ]
CMD ["Mockserver/api_call.py"]