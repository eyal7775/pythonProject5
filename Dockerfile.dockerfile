FROM python:latest
LABEL version="1.0"
COPY requirements.txt ./
RUN pip install -r requirements.txt
ENV FILE_NAME logfilename
ENV MY_IP_SERVER 10.0.2.42
ENV MY_IP_JSON 10.0.2.30
WORKDIR /usr/app/src
COPY json_format.py ./
ENV TZ="Asia/Jerusalem"
ENTRYPOINT ["python" ,"json_format.py"]
