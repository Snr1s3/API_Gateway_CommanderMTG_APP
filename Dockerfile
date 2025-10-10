FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Simple fix: use trusted hosts
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt



COPY SRC/ ./SRC/

EXPOSE 8441

# Run the application
CMD ["uvicorn", "SRC.main:app", "--host", "0.0.0.0", "--port", "8441"]