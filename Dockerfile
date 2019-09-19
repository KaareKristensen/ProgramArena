FROM python:3.7
LABEL maintainer="mmedum@gmail.com"

EXPOSE 80

RUN pip install fastapi uvicorn

COPY ./app /app

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR ./
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
