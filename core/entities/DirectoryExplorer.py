import os
import sys
from core.entities.implementations.DirectoryExplorerImplementation import  DirectoryExplorerImplementation


class DirectoryExplorer:
    def __init__(self, directory=None):
        self.implementation = DirectoryExplorerImplementation()
        self.directory = directory
        if directory is None:
            self.directory = os.getcwd()

    def list_files(self, extension=None):
        return self.implementation.list_files(self.directory, extension)

    def list_folders(self, folder=None):
        return self.implementation.list_folders(self.directory, folder)

    def find_only_file(self, file):
        return self.implementation.find_only_file(self.directory, file)
