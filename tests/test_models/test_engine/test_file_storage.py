#!/use/bin/python3
""" Defines Unittests for models/engine/file_storage.py
"""

import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """ Unittests for testing the instantiation
    of the FileStorage class. """

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_Instantiation_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.Testcase):
    """ Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage.__FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        ci = City()
        am = Amenity()
        re = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(ci)
        models.storage.new(am)
        models.storage.new(re)
        kys = models.storage.all().keys()
        vals = models.storage.all().values()
        self.assertIn("BaseModel." + bm.id, kys)
        self.assertIn("Basemodel." + bm.id, vals)
        self.assertIn("User." + us.id, kys)
        self.assertIn("User." + us.id, vals)
        self.assertIn("State." + st.id, kys)
        self.assertIn("State." + st.id, vals)
        self.assertIn("Place." + pl.id, kys)
        self.assertIn("Place." + pl.id, vals)
        self.assertIn("City." + ci.id, kys)
        self.assertIn("City." + ci.id, vals)
        self.assertIn("Amenity." + am.id, kys)
        self.assertIn("Amenity." + am.id, vals)
        self.assertIn("Review." + re.id, kys)
        self.assertIn("Review." + re.id, vals)

    def test_new_with_args(self):
        with self.assertRaise(TypeError):
            models.storage.new(Basemodel(), 1)

    def test_save(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        ci = City()
        am = Amenity()
        re = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(ci)
        models.storage.new(am)
        models.storage.new(re)
        models.storage.save()
        save_text = ""
        with open("file.jason", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + ci.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + re.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        ci = City()
        am = Amenity()
        re = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(ci)
        models.storage.new(am)
        models.storage.new(re)
        models.storage.save()
        models.storage.reload()
        obj = FileStorage.__Filestorage__objects
        self.assertIn("BaseModel." + bm.id, obj)
        self.assertIn("User." + us.id, obj)
        self.assertIn("State." + st.id, obj)
        self.assertIn("Place." + pl.id, obj)
        self.assertIn("City." + ci.id, obj)
        self.assertIn("Amenity." + am.id, obj)
        self.assertIn("Review." + re.id, obj)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
