# syntax=docker/dockerfile:1

FROM python:3.8-alpine
# setting working dir
WORKDIR /"infra-cloud"
# adding contents to container
ADD . /"infra-cloud"
# running reuirements.txt
RUN pip3 install -r requirements.txt