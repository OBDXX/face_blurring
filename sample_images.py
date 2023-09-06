import os
import requests

def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download {url}")

def main():
    # Create a directory to save the images
    save_dir = "sample_images"
    os.makedirs(save_dir, exist_ok=True)

    # Base URL for LFW dataset
    base_url = "http://vis-www.cs.umass.edu/lfw/images/"

    # Sample names (you can change these to any names available in the LFW dataset)
    names = [
        "George_W_Bush",
        "Colin_Powell",
        "Tony_Blair",
        "Donald_Rumsfeld",
        "Gerhard_Schroeder"
    ]

    # Download 10 images for each name (total 50 images)
    for name in names:
        for i in range(1, 11):
            img_name = f"{name}_{str(i).zfill(4)}.jpg"
            img_url = f"{base_url}{name}/{img_name}"
            save_path = os.path.join(save_dir, img_name)
            download_image(img_url, save_path)
            print(f"Downloaded {img_name}")

if __name__ == "__main__":
    main()