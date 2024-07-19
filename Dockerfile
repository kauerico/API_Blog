FROM python:3.12.4

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./codigo/ /app

EXPOSE 8000

CMD ["fastapi", "dev", "./codigo/main.py"]