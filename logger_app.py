import task_1                      # FlatIterator из д/з лекции 2
import task_4                      # flat_generator из д/з лекции 2
from task_2 import logger          # параметризованный декоратор из этого д/з


@logger('app.log')
def flat_with_iterator(list_of_lists):
    """Плоское представление списка списков через итератор FlatIterator."""
    return list(task_1.FlatIterator(list_of_lists))


@logger('app.log')
def flat_with_generator(list_of_lists):
    """Плоское представление списка списков через генератор flat_generator."""
    return list(task_4.flat_generator(list_of_lists))


if __name__ == '__main__':
    data = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    print(flat_with_iterator(data))
    print(flat_with_generator(data))

    print('\n--- Содержимое app.log ---')
    with open('app.log', encoding='utf-8') as f:
        print(f.read())