FROM python:3.10-slim
WORKDIR /app
COPY app.py .
RUN pip install flask prometheus-client && pip cache purge
CMD ["python", "app.py"]


