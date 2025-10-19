from Terminal import *
from pathlib import Path

manager = FileSystem.FileManager(FileSystem.Directory.load(Path("test")))
manager.print()
manager.input()
manager.print()
manager.input()
manager.print()
manager.input()
manager.print()