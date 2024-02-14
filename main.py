import os
from core.entities.output.OutputHandler import OutputHandler
from core.entities.DirectoryExplorer import DirectoryExplorer

dir = DirectoryExplorer(os.getcwd())
#dir.find_files_ignoring_this_folder("teste.txt", "pasta")
#json = dir.find_only_file("configCae.json")
#print(dir.read_file(json))

"""folders = dir.list_folders("use_cases")
print(len(folders))
folders = dir.find_folders_ignoring_this_folder("use_cases","target")
print(len(folders))"""

output = OutputHandler
output.success_message("Um texto é uma manifestação da linguagem. Pode ser definido como tudo aquilo que é dito por um emissor e interpretado por um receptor. Dessa forma, tudo que é interpretável é um texto. Outra forma de conceituação é pensar que tudo aquilo que produz um sentido completo, que seja uma mensagem compreensível, é um texto.")
output.information_message("Olá! Sim, estou bem, obrigado! Como posso ajudar você hoje?")


files = dir.list_files("asd.json")
dir.find_only_file(".java")
print(files)

