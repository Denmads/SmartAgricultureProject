import uuid
from dronecontroller import DroneController
from backendapi import BackendAPI
import sys, glob, base64

def load_images() -> list[str]:
    images = []
    for filename in glob.glob("images/*.png"):
        with open(filename, "rb") as img:
            encoded = base64.b64encode(img.read())
            images.append(encoded.decode('utf-8'))
    return images
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: <api_base_url>")
        exit(1)
    
    id = str(uuid.uuid4())
    backend = BackendAPI(sys.argv[1])
    images = load_images()
    
    controller = DroneController(id, backend, images)
    controller.boot()