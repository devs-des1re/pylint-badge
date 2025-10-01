FROM python:3.11-slim

WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your action code
COPY main.py .

# Set the entrypoint
ENTRYPOINT ["python", "/app/main.py"]
