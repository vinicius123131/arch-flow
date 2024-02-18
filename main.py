import os
from core.entities.output.OutputHandler import OutputHandler
from core.entities.DirectoryExplorer import DirectoryExplorer
from core.entities.StringManipulator import StringManipulator
from core.entities.DirectoryCreator import DirectoryCreator

creator = DirectoryCreator()
path = "/home/vinicius/Documentos/projetos/pessoal/arch-flow/core/entities/teste/"
file_name = 'teste1.txt'
file_conteudo = 'teste de criação de arquivo\nquebra de linha'
creator.create_file(path, file_name, file_conteudo, True)
input()

print(creator.does_file_or_directory_exist(path))
creator.create_folder(path)
input()

string_manipulator = StringManipulator()
use_case ='novo caso de uso'
def name(name):
    return use_case

tag_user = {
    'name': name
}
texto_original = ("<pc><name> use case assembler</pc>.java\n"
                  "<sc><name></sc>\n"
                  "<asd>teste <sc><name> normal por aqui</sc> <hh></hh> </asd>")

result =string_manipulator.replace_tags(texto_original, tag_user)
print(result)
input()


#teste = ["novo", "caso", "de", "Uso-teste"]
teste = "novo caso_deUso-teste"
print(f"Original: {teste}")
print(f"PascalCase: {string_manipulator.to_pascal_case(teste)}")
print(f"CamelCase: {string_manipulator.to_camel_case(teste)}")
print(f"SnakeCase: {string_manipulator.to_snake_case(teste)}")
print(f"KebabCase: {string_manipulator.to_kebab_case(teste)}")
print(f"FlatCase: {string_manipulator.to_flat_case(teste)}")
print(f"UpperFlatCase: {string_manipulator.to_upper_flat_case(teste)}")
print(f"PascalSnakeCase: {string_manipulator.to_pascal_snake_case(teste)}")
print(f"CamelSnakeCase: {string_manipulator.to_camel_snake_case(teste)}")
print(f"ScreamingSnakeCase: {string_manipulator.to_screaming_snake_case(teste)}")
print(f"TrainCase: {string_manipulator.to_train_case(teste)}")
print(f"CobolCase: {string_manipulator.to_cobol_case(teste)}")

dir = DirectoryExplorer(os.getcwd())
dir.find_files_ignoring_this_folder("teste.txt", "pasta")
json = dir.find_only_file("configCae.json")
print(dir.read_file(json))

folders = dir.list_folders("use_cases")
print(len(folders))
folders = dir.find_folders_ignoring_this_folder("use_cases","target")
print(len(folders))

output = OutputHandler
output.success_message("Um texto é uma manifestação da linguagem. Pode ser definido como tudo aquilo que é dito por um emissor e interpretado por um receptor. Dessa forma, tudo que é interpretável é um texto. Outra forma de conceituação é pensar que tudo aquilo que produz um sentido completo, que seja uma mensagem compreensível, é um texto.")
output.information_message("Olá! Sim, estou bem, obrigado! Como posso ajudar você hoje?")


files = dir.list_files("asd.json")
dir.find_only_file(".java")
print(files)

