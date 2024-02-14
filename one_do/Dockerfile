FROM python:3.12-alpine3.18

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py ./
COPY data1.csv ./
COPY data2.csv ./

CMD ["python", "./server.py"]
