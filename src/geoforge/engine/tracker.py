import json
import os
from datetime import datetime

TRACK_FILE = "tracking.json"


def save_result(prompt, result):
    entry = {
        "timestamp": str(datetime.now()),
        "prompt": prompt,
        "result": result
    }

    data = []

    if os.path.exists(TRACK_FILE):
        with open(TRACK_FILE, "r") as f:
            data = json.load(f)

    data.append(entry)

    with open(TRACK_FILE, "w") as f:
        json.dump(data, f, indent=2)