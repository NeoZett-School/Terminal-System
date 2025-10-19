from .files import File, Directory, FileManager
from .enums import ItemType

class FileSystem:
    File = File
    Directory = Directory
    FileManager = FileManager
    ItemType = ItemType

__all__ = ("FileSystem",)