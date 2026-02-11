FROM python:3.10-slim

COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.4 /lambda-adapter /opt/extensions/lambda-adapter

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip && python -m pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "RiotAPIproject.wsgi:application"]