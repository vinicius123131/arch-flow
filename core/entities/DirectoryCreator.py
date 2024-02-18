import os.path

from core.entities.implementations.DirectoryCreatorImplementation import DirectoryCreatorImplementation


class DirectoryCreator:

    def __init__(self):
        self.implementation = DirectoryCreatorImplementation()

    def does_file_or_directory_exist(self, path):
        return self.implementation.does_file_or_directory_exist(path)

    def create_folder(self, folder_path):
        return self.implementation.create_folder(folder_path)