import json
from typing import Dict


class Analyzer:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.data = self._read_annotations()
        self.categories = self.data["categories"]

    def _read_annotations(self) -> Dict:
        with open(self.filename, "r") as f:
            data = json.load(f)

        return data

    def _get_category_id(self, name: str) -> int:
        category_id = None

        for category in self.categories:
            if category["name"] == name:
                category_id = category["id"]
                break

        return category_id
