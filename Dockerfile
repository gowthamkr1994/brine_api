FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /code/
COPY ./schema.sql /docker-entrypoint-initdb.d/
RUN chmod +x entrypoint1.sh
COPY ./brine_db.sql /docker-entrypoint-initdb.d/