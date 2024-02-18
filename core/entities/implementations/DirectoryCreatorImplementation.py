import os.path
from core.entities.exceptions.FileOrDirectoryExistsError import FileOrDirectoryExistsError
from core.entities.output.OutputHandler import OutputHandler

exception = FileOrDirectoryExistsError()
output = OutputHandler()


class DirectoryCreatorImplementation:
    @staticmethod
    def does_file_or_directory_exist(path):
        return os.path.exists(path)

    @staticmethod
    def create_folder(folder_path):
        try:
            os.makedirs(folder_path)
            output.success_message(f"folder '{folder_path}' created successfully")
        except FileExistsError:
            exception.already_exists_error(f"the folder '{folder_path}' already exists")
        except Exception as e:
            exception.fatal_error(f"error creating folder '{folder_path}' exception: {e}")
