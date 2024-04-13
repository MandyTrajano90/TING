def exists_word(word, instance):
    results = list()
    for item in instance.queue:
        path_name = item["nome_do_arquivo"]
        word_exists = list()
        for line_number, line in enumerate(item["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                word_exists.append({"linha": line_number})
        if word_exists:
            results.append({
                "palavra": word,
                "arquivo": path_name,
                "ocorrencias": word_exists
            })
    return results


def search_by_word(word, instance):
    results = list()
    for item in instance.queue:
        path_name = item["nome_do_arquivo"]
        word_exists = list()
        for line_number, line in enumerate(item["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                word_exists.append(
                    {"linha": line_number, "conteudo": line.strip()}
                )
        if word_exists:
            results.append({
                "palavra": word,
                "arquivo": path_name,
                "ocorrencias": word_exists
            })
    return results
