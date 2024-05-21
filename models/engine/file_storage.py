#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        _dict = {}
        for key, val in FileStorage.__objects.items():
            _dict[key] = val.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as file:
                deserialize = json.load(file)
                if deserialize is None:
                    return
                for obj in deserialize.values():
                    if obj is None:
                        continue
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
