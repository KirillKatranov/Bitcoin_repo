FROM python:3.11.9-alpine

WORKDIR /app
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip

COPY requirements_src.txt .

 
RUN pip install --no-cache-dir -r requirements_src.txt

COPY . .

#CMD ["python", "BTCN_price.py"]

