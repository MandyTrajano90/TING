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
    """Aqui irá sua implementação"""
