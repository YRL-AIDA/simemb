import requests
import json
import numpy as np
from src.settings import settings

if __name__ == "__main__":
    request = "text_req.json"
    if settings.use_vl:
        request = "vl_req.json"

    with open(request) as f:
        payload = json.load(f)

    response = requests.post(
        f"http://{settings.service_address}:{settings.service_port}/embedding/embed",
        json=payload
    )

    embeddings = json.loads(response.json())["embeddings"]

    filename = "response.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump({"embeddings": embeddings}, f, indent=2, ensure_ascii=False)
    print(np.array(embeddings).shape)
