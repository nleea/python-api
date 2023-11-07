FROM python:3

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/ /code/app/

EXPOSE 8000

ENTRYPOINT ["uvicorn"]

CMD ["app.main:app", "--reload","--host", "0.0.0.0", "--port", "8000"]
