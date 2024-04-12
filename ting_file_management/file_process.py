from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    txt_importer(path_file)

    if any(file_name == path_file for file_name in instance.queue):
        return

    instance.enqueue(path_file)
    dict_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }
    sys.stdout.write(f"{dict_data}\n")


def remove(instance):
    if len(instance.queue) == 0:
        sys.stdout.write("Não há elementos\n")
        return
    deleted_file = instance.dequeue()
    print(f"Arquivo {deleted_file} removido com sucesso")


def file_metadata(instance, position):
    if position < 0 or position >= len(instance.queue):
        sys.stderr.write("Posição inválida\n")
        return
    file_name = instance.search(position)
    dict_data = {
        "nome_do_arquivo": file_name,
        "qtd_linhas": len(txt_importer(file_name)),
        "linhas_do_arquivo": txt_importer(file_name),
    }
    sys.stdout.write(f"{dict_data}\n")
