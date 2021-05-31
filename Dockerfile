FROM python:3
MAINTAINER admin
USER root
WORKDIR /app
ADD . /app
RUN apt update && apt install --no-install-recommends -y python3-dev  gcc build-essential
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install --no-cache-dir tensorflow
EXPOSE 8080
ENTRYPOINT ["python", "app.py"]