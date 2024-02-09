import os

from core.entities.DirectoryExplorer import DirectoryExplorer

dir = DirectoryExplorer(os.getcwd())
files = dir.list_files()
print(files)