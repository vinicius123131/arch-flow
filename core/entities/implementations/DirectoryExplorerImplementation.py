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
            message_error = f"files with name or extension '{extension}' on directory '{directory}' is null" if extension else \
                f"files on directory '{directory}' is null"
            return NotFoundException.not_found_error(message_error)
        return files

    @staticmethod
    def list_folders(directory, folder=None):
        folders = [os.path.join(directory, d) for d in os.listdir(directory) if
                   os.path.isdir(os.path.join(directory, d))]

        if folder is not None:
            folders = [f for f in folders if os.path.basename(f) == folder]

        if len(folder) == 0:
            return NotFoundException.not_found_error(f"")
        return folders

    @staticmethod
    def find_only_file(directory, file):
        files = DirectoryExplorerImplementation.list_files(directory, file)
        qtde_files = len(files)
        if qtde_files == 0 or qtde_files >= 2:
            print("Muitos arquivos encontrados, erro na busca única")
            sys.exit(1)
        return files
