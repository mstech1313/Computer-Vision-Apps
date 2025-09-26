from flask import Flask, request, jsonify, send_from_directory
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import os

app = Flask(__name__, static_folder='../static', static_url_path='')

AZURE_ENDPOINT = os.getenv('AZURE_ENDPOINT', 'YOUR_AZURE_ENDPOINT')
AZURE_KEY = os.getenv('AZURE_KEY', 'YOUR_AZURE_KEY')

computervision_client = ComputerVisionClient(AZURE_ENDPOINT, CognitiveServicesCredentials(AZURE_KEY))

@app.route('/api/analyze-image', methods=['POST'])
def analyze_image():
    image_file = request.files['image']
    analysis = computervision_client.describe_image_in_stream(image_file)
    description = ""
    if analysis.captions:
        description = analysis.captions[0].text
    return jsonify({"description": description})

@app.route('/')
def serve_home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)