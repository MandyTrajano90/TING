from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    text = txt_importer(path_file)

    if any(item["nome_do_arquivo"] == path_file for item in instance.queue):
        return

    dict_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text),
        "linhas_do_arquivo": text,
    }
    instance.enqueue(dict_data)
    sys.stdout.write(f"{dict_data}\n")


def remove(instance):
    if len(instance.queue) == 0:
        sys.stdout.write("Não há elementos\n")
        return
    dict_data = instance.dequeue()
    return_dict = dict_data["nome_do_arquivo"]
    print(f"Arquivo {return_dict} removido com sucesso")


def file_metadata(instance, position):
    if position < 0 or position >= len(instance.queue):
        sys.stderr.write("Posição inválida\n")
        return
    dict_data = instance.search(position)
    sys.stdout.write(f"{dict_data}\n")
