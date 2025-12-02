import json

class FileSystem:
    def load_disk(self):
        disk_path = "F:\\Khaled\\LightsOS\\data\\disk.json"
        with open(disk_path, 'r') as f:
            full_disk = json.load(f)
            return full_disk