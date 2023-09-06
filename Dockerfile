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
RUN git clone https://github.com/OBDXX/face_blurring.git

# Set the working directory
WORKDIR /face_blurring

# Install Python dependencies
RUN pip install -r req.txt

# Define the entry point for running the blurring script
CMD ["python", "blur_faces.py"]

