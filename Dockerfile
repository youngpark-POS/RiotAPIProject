FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/
RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt

COPY . /app/
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "RiotAPIproject.wsgi:application"]