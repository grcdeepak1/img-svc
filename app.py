from flask import Flask, request, jsonify
import os
import base64

app = Flask(__name__)
IMG_PATH = os.environ.get("IMG_PATH", "images/")

def base64_encode(img_path):
    """
    Returns base64 encoded image.

    Args:
        img_path (str): The path to the image

    Returns:
        str: The base64 encoded image
    """
    with open(img_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        return f"{encoded_string}"

@app.route('/', methods=['POST'])
def process_input():
    image = ""
    output_images = "pic1.jpg"
    local_image_path = f"{IMG_PATH}/{output_images}"
    if os.path.exists(local_image_path):
        image = base64_encode(local_image_path)
    response = {
        "status": "success",
        "message": image,
    }
    return jsonify(response), 200



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
