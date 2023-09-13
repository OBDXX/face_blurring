import cv2
import os

from face_blurring import create_parser
print("Face blurring completed!")
parser = create_parser()
args = parser.parse_args()

print(f"Reading from {args.input} and writing to {args.output}")

def blur_faces(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)

    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

    # Loop through the coordinates of detected faces and blur them
    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        blurred_face = cv2.GaussianBlur(face, (99, 99), 30)
        image[y:y+h, x:x+w] = blurred_face

    # Save the image with blurred faces
    cv2.imwrite(output_path, image)

def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(args.input):
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            blur_faces(args.input, args.output)
            print(f"Processed {filename}")

if __name__ == "__main__":
    input_folder = args.input  # Replace with the path to your folder containing images
    output_folder = args.output  # Replace with the path where you want to save images with blurred faces

    process_folder(input_folder, output_folder)

