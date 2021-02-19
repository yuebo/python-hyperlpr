import cv2
from flask import Flask, Response, request
from hyperlpr import *
import numpy as np
import json

app = Flask(__name__)


@app.route('/', methods=['get'])
def index():
    return Response("It works!")


@app.route('/', methods=['post'])
def recognition():
    print(request)
    image = cv2.imdecode(np.frombuffer(request.data, np.uint8), 1)
    result = HyperLPR_plate_recognition(image)
    return Response(json.dumps(result), mimetype='application/json')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
