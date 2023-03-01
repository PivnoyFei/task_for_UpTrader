FROM python:3.11.0-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /backend

COPY . .

RUN apt-get update && apt-get install gcc libpq-dev -y
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]