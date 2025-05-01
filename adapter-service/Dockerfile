FROM python:3.10-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
RUN pip install flask-cors
CMD ["python", "app.py"]