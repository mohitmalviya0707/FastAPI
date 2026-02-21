import json
from pathlib import Path
from typing import List, Dict

# Correct file path: Go 2 folders up (service → app → fasst api)
DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "products.json"

def load_products() -> List[Dict]:
    if not DATA_FILE.exists():
        return []
    
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def get_all_products() -> List[Dict]:
    return load_products()