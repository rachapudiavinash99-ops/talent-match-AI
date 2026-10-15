import json
import os
import uuid
from typing import List, Dict, Optional
from filelock import FileLock

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

class JSONRepository:
    def __init__(self, filename: str):
        self.filename = filename
        self.filepath = os.path.join(DATA_DIR, f"{filename}.json")
        self.lockpath = os.path.join(DATA_DIR, f"{filename}.json.lock")
        
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
            
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _read_data(self) -> List[Dict]:
        with FileLock(self.lockpath):
            try:
                with open(self.filepath, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []

    def _write_data(self, data: List[Dict]):
        with FileLock(self.lockpath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)

    def get_all(self) -> List[Dict]:
        return self._read_data()

    def get_by_id(self, item_id: str) -> Optional[Dict]:
        data = self._read_data()
        for item in data:
            if item.get("id") == item_id:
                return item
        return None

    def create(self, item: Dict) -> Dict:
        data = self._read_data()
        if "id" not in item:
            item["id"] = str(uuid.uuid4())
        data.append(item)
        self._write_data(data)
        return item

    def update(self, item_id: str, updated_fields: Dict) -> Optional[Dict]:
        data = self._read_data()
        for idx, item in enumerate(data):
            if item.get("id") == item_id:
                data[idx].update(updated_fields)
                self._write_data(data)
                return data[idx]
        return None

    def delete(self, item_id: str) -> bool:
        data = self._read_data()
        new_data = [item for item in data if item.get("id") != item_id]
        if len(data) != len(new_data):
            self._write_data(new_data)
            return True
        return False
