import json
import requests
import os


UPLOAD_IMAGES_URL = "http://localhost:8000/upload-image"

texts = [
    "A woman playing with her dog on a beach at sunset."
]

images = [
    "/home/kirilltobola/Downloads/demo.jpeg",
]


def upload_images():
    for image_path in images:
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                files = {'file': (os.path.basename(image_path), f, 'image/jpeg')}
                response = requests.post(UPLOAD_IMAGES_URL, files=files)
                print(response.json())
        else:
            print(f"Error: {image_path} not found.")


def generate_vl_request(texts: list[str], images: list[str], filename: str = "vl_req.json") -> list[dict]:
    documents = [{"text": text} for text in texts]
    documents += [
        {"image": "uploads/" + os.path.basename(img_path)} for img_path in images
    ]

    with open(filename, "w", encoding="utf-8") as f:
        json.dump({"documents": documents}, f, indent=2, ensure_ascii=False)
    print(f"Generated  '{filename}' with {len(texts) + len(images)} requests.")


if __name__ == "__main__":
    upload_images()
    generate_vl_request(texts, images)
