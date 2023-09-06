# Use a base image with Python and OpenCV installed
FROM python:3.8

# Set environment variables for non-interactive mode
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary system packages
RUN apt-get update && apt-get install -y \
    cmake \
    git \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Clone your face-blurring project repository
RUN git clone https://github.com/yourusername/your-face-blurring-project.git /app

# Set the working directory
WORKDIR /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy your face-blurring script into the container
COPY blur_faces.py /app/blur_faces.py

# Define the entry point for running the blurring script
CMD ["python", "blur_faces.py"]

