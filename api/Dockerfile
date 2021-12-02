FROM python:3.8.0-slim

WORKDIR /usr/src/transaction/api/app

COPY ./app/requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . /usr/src/transaction/api/

CMD ["uvicorn", "--reload", "main:app", "--host", "0.0.0.0"]