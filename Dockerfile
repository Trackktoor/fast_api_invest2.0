FROM python:3.11

RUN apt update && apt upgrade -y
RUN python3.11 -m pip install --upgrade pip setuptools

WORKDIR /invest
COPY ./requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY ./ .
CMD [ "uvicorn",  "src.main:create_app", "--host", "0.0.0.0", "--port", "80",  "--reload"]