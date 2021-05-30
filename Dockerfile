FROM python:3.5-slim
MAINTAINER admin
USER root
WORKDIR /app
ADD . /app
RUN yum update && tum install --no-install-recommends -y python3-dev  gcc build-essential
EXPOSE 8080
ENTRYPOINT ["python", "app.py"]