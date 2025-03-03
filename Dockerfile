# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /home

# Copy necessary files
COPY scripts/scripts.py /home/scripts/scripts.py
COPY data /home/data

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the script when the container starts
CMD ["python3", "/home/scripts/scripts.py"]

