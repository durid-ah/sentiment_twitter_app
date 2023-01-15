FROM python:3.11.1-slim
WORKDIR /app

RUN apt-get update \
   && apt-get --assume-yes install freetds-dev freetds-bin

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]