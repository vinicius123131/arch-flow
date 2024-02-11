import os
import sys

from core.entities.exceptions.NotFoundException import NotFoundException


class DirectoryExplorerImplementation:
    @staticmethod
    def list_files(directory, extension=None):
        files = []
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                if extension is None or filename.endswith(extension):
                    files.append(os.path.join(root, filename))
        if len(files) == 0:
            message_error = f"files with name or extension '{extension}' on directory '{directory}' is None" \
                if extension else \
                f"this directory '{directory}' is empty"
            return NotFoundException.not_found_error(message_error)
        return files

    @staticmethod
    def list_folders(directory, folder=None):
        folders = [os.path.join(directory, d) for d in os.listdir(directory) if
                   os.path.isdir(os.path.join(directory, d))]

        if folder is not None:
            folders = [f for f in folders if os.path.basename(f) == folder]

        if len(folder) == 0:
            message_error = f"folders with name '{folder}' on directory '{directory}' is None" \
                if folder else \
                f"this directory '{directory}' is empty"
            return NotFoundException.not_found_error(message_error)
        return folders

    @staticmethod
    def find_only_file(directory, file):
        files = DirectoryExplorerImplementation.list_files(directory, file)
        qtde_files = len(files) if files is not None else 0
        if qtde_files == 0:
            return NotFoundException.fatal_not_found_error(f"File '{file}' could not be located in the specified "
                                                           f"directory '{directory}'. This file is essential for "
                                                           f"the proper functioning of the application.")
        if qtde_files >= 2:
            return NotFoundException.fatal_not_found_error(f"Multiple files with the name '{file}' have been found "
                                                           f"in the directory '{directory}'. It is highly advisable "
                                                           f"to have only one file with this name to ensure the "
                                                           f"optimal functioning of the application.")
        return files
