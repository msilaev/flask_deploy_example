FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install any needed dependencies specified in requirements.txt
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
