""" This module initializes the storage variable to be used in projects"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

__all__ = ["storage"]
