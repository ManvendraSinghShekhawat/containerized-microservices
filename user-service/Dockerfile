# user-service/Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
# Use gunicorn in production, but allow flask dev when running locally via python
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "2"]

