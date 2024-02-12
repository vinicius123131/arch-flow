import os
from core.entities.output.OutputHandler import OutputHandler
from core.entities.DirectoryExplorer import DirectoryExplorer

output = OutputHandler
output.success_message("A criação de pasta foi realizada com sucesso pasta 'teste/cae/teasdfasd'")
output.information_message("Olá! Sim, estou bem, obrigado! Como posso ajudar você hoje?")
dir = DirectoryExplorer(os.getcwd())

files = dir.list_files("asd.json")
dir.find_only_file(".java")
print(files)

