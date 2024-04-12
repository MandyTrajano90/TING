from ting_file_management.priority_queue import PriorityQueue
import pytest


def create_instances(list, instance):
    for index in range(len(list)):
        new_item = {
            "nome_do_arquivo": f"arquivo_{index}.txt",
            "qtd_linhas": list[index],
            "linhas_do_arquivo": ["Hello World"],
        }
        instance.enqueue(new_item)


def checkListOrder(instance):
    size_list = []
    for index in range(len(instance)):
        size_list.append(instance.search(index)["qtd_linhas"])
    return size_list


def test_basic_priority_queueing():
    PriorityQueueList = PriorityQueue()
    entrys = [9, 4, 2, 5, 7, 11, 3]

    create_instances(entrys, PriorityQueueList)
    new_list = checkListOrder(PriorityQueueList)
    assert new_list == [4, 2, 3, 9, 5, 7, 11]
    assert new_list != entrys
    PriorityQueueList.dequeue()
    assert checkListOrder(PriorityQueueList) == [2, 3, 9, 5, 7, 11]

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        PriorityQueueList.search(10)


if __name__ == "__main__":
    test_basic_priority_queueing()
