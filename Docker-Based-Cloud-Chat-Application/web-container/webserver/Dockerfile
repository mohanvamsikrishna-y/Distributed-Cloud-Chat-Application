FROM python:3.8-slim
WORKDIR /app
#copy requirements file
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
#start flask app
CMD ["python3", "run.py"]


