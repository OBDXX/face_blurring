import os
import subprocess
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description="A simple argparse example.")
    parser.add_argument("--input", type=str, required=True,
                    help="path to a single image or image directory")
    return parser

parser = create_parser()
args = parser.parse_args()

# Build the Docker image
subprocess.run(["docker", "build", "-t", "face-blurring-app", "."])

# Define input and output directories
input_dir = args.input
output_dir = "output_images"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Run the Docker container to process images
subprocess.run(["docker", "run", "-v", f"{os.path.abspath(input_dir)}:/app/input_images","-v", f"{os.path.abspath(output_dir)}:/app/output_images", "face-blurring-app"])

print("Face blurring completed!")

