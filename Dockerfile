
FROM python:3.10.6

WORKDIR /app-pro

COPY . /app-pro

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]

