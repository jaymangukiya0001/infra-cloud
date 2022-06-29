FROM python:3.8
# setting working dir
WORKDIR /"infra-cloud"
COPY . .
# running reuirements.txt
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["Mockserver/api_call.py"]