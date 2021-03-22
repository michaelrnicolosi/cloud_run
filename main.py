
import base64
import os
import requests 
from google.cloud import storage
from io import StringIO
import pandas as pd
import json

from flask import Flask, request


app = Flask(__name__)

# Allow POST requests to your endpoint
@app.route("/", methods=["POST"])
def index():
   
    # GA Server Enpoint
    ENDPOINT = "https://www.google-analytics.com/collect?v=1&t=event&tid=UA-XXXXXXXX-Y&cid=4cacd0f6-2c8c-4fd0-93c2-1bf68d2c8760&ec=test&ua=32"
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('<YOUR-GCS-BUCKET>')
    file_name = json.loads(name)["name"]
    blob = bucket.get_blob(file_name)
    data = blob.download_as_string()
    s = str(data, "utf-8")
    s = StringIO(s)
    df = pd.read_csv(s)
    
    for row in df['event']:
        url = ENDPOINT + "&ea=" + row
        r = requests.post(url)

    return ("", 204)

if __name__ == "__main__":
    PORT = int(os.getenv("PORT")) if os.getenv("PORT") else 8080
    app.run(host="127.0.0.1", port=PORT, debug=True)
