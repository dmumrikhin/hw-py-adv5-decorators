'''
Применить написанный логгер к приложению из любого предыдущего д/з.
'''

import os
import datetime



def logger(old_function):
    file = []
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        string = (f'{old_function.__name__} {str(datetime.datetime.now())} {args} {kwargs} {result}\n')
        with open('task_3.log', 'a') as f:
            f.write(string)    
        return result
    return new_function

import types

@logger
def flat_generator(list_of_lists):
    for elem in list_of_lists:
        yield from elem

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 
        'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()

