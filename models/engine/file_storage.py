#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ Represents an abstract storage engine.

    Attributes:
    __file_path (str): The name of the file to save objects to.
    __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """ Set obj with key <obj_class_name>.id. """
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """ Serialize  __objects to the JSON file __file__path. """
        obj_dict = FileStorage.__objects
        odict = {}

        for obj in obj_dict.keys():
            odict[obj] = obj_dict[obj].to_dict()
            
        with open(FileStorage.__file_path, "w", encoding="utf-8") as j:
            json.dump(odict, j)


    def reload(self):
        """ Deserialize JSON file __file__path to __objects. """
        try:
            with open(FileStorage.__file_path) as j:
                odict = json.load(j)
                for i in odict.values():
                    cls_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cls_name)(**i))
        except FileNotFoundError:
            return
