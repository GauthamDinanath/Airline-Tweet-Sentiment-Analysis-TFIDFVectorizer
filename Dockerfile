FROM python:3.5-slim
MAINTAINER admin
USER root
WORKDIR /app
ADD . /app
RUN yum update && yum install --no-install-recommends -y python3-dev  gcc build-essential
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python", "app.py"]