import cv2
from PIL import Image
import torch
from transformers import AutoModelForImageClassification, ViTImageProcessor

model = AutoModelForImageClassification.from_pretrained("Falconsai/nsfw_image_detection")
processor = ViTImageProcessor.from_pretrained('Falconsai/nsfw_image_detection')

def getimage():
    print("Enter the file path of the image: ")
    while True:
        path = input()
        if path:
            break
    if path.endswith(".png") or path.endswith(".jpg") or path.endswith(".jpeg"):
        try:
            img = Image.open(path)
        except Exception as e:
            print("Invalid file path. Error: ", e)
            return
        with torch.no_grad():
            inputs = processor(images=img, return_tensors="pt")
            outputs = model(**inputs)
            logits = outputs.logits

        predicted_label = logits.argmax(-1).item()
        if predicted_label:
            print("NSFW")
        else:
            print("Not NSFW")
    
    elif path.endswith(".mp4") or path.endswith(".webm"):
        videoShit(path)
    
    else:
        print("Invalid file format")

def capture_screenshot(path):
    vidObj = cv2.VideoCapture(path)
    fps = vidObj.get(cv2.CAP_PROP_FPS)
    frames_to_skip = int(fps * 10)

    count = 0
    success = 1
    saved_image_names = []

    while success:
        success, image = vidObj.read()
        if frames_to_skip > 0 and count % frames_to_skip == 0:
            image_name = f"image_{count // frames_to_skip}.png"
            cv2.imwrite(image_name, image)
            saved_image_names.append(image_name)

        count += 1

    vidObj.release()
    
    return saved_image_names


def videoShit(video_path):
    imageName = capture_screenshot(video_path)
    for cum in imageName:
        img = Image.open(cum)
        with torch.no_grad():
            inputs = processor(images=img, return_tensors="pt")
            outputs = model(**inputs)
            logits = outputs.logits

        predicted_label = logits.argmax(-1).item()
        if predicted_label:
            print("NSFW")
        else:
            print("Not NSFW")


if __name__ == "__main__":
    getimage()