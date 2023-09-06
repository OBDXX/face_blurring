import os
import subprocess

# Build the Docker image
subprocess.run(["docker", "build", "-t", "face-blurring-app", "."])

# Define input and output directories
input_dir = "input_images"
output_dir = "output_images"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Run the Docker container to process images
subprocess.run(["docker", "run", "-v", f"{os.path.abspath(input_dir)}:/app/input_images","-v", f"{os.path.abspath(output_dir)}:/app/output_images", "face-blurring-app"])

print("Face blurring completed!")

