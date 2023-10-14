# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install the ShoppingBot package and its dependencies
RUN pip install --upgrade pip \
    && pip install .

# Run your application
CMD ["python", "main.py"]
