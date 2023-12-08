#!/usr/bin/python3
""" Magic method for models directory. """
from models.file_storage import FileStorage

storage = FileStorage()
storage.reload()
