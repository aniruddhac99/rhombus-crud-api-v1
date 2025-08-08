FROM python:3.10-slim
WORKDIR /app
COPY app.py .
RUN pip install flask prometheus-client && pip cache purge
CMD ["python", "app.py"]


# Secure Dockerfile practices (non-root user, minimized base image, etc.)
# Build the image and run it locally in Docker env and verify the endpoints.
