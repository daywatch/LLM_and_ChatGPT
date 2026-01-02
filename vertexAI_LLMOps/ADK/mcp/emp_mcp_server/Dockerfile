# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your server code
COPY server.py .

# Expose Cloud Run port
EXPOSE 8080

# Run the MCP server
CMD ["python", "server.py"]


