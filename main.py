import os

from core.entities.DirectoryExplorer import DirectoryExplorer

dir = DirectoryExplorer(os.getcwd())

files = dir.list_files("asd.json")
print("📗 Teste para saber se para o ")
dir.find_only_file(".java")
print(files)

