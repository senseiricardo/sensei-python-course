import json
import os
from config.config import USER_JSON_PATH

def load_users():
    path = os.path.join(os.path.dirname(__file__), USER_JSON_PATH)
    with open(path) as f:
        return json.load(f)