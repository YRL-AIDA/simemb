import json
import requests
import os


texts = [
    "A woman playing with her dog on a beach at sunset."
]

images = [
    "/home/kirilltobola/Downloads/demo.jpeg",
]


def upload_images():
    global images
    api_url = "http://localhost:8000/upload-image"
    for image_path in images:
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                files = {'file': (os.path.basename(image_path), f, 'image/jpeg')}
                response = requests.post(api_url, files=files)
                print(response.json())
        else:
            print(f"Error: {image_path} not found.")


def generate_vl_request(filename: str = "vl_req.json") -> list[dict]:
    global texts, images
    queries = []

    for text in texts:
        queries.append({"text": text})
    for image_path in images:
        queries.append({"image": "uploads/" + os.path.basename(image_path)})

    with open(filename, "w", encoding="utf-8") as f:
        json.dump({"inputs": queries}, f, indent=2, ensure_ascii=False)
    print(f"Generated  '{filename}' with {len(queries)} requests.")


if __name__ == "__main__":
    upload_images()
    generate_vl_request()
