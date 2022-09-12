import pytest


# входящее значение является int
def test_int_1(i=5):
    assert isinstance(i, int), 'Not int'


# проверка на то, что входное значение является целым числом
# придумываем требования сами
# допустим, требования к значению от -10 до 10, в таком случае проверяем граничные значения
# с учётом классов эквивалентности
@pytest.mark.parametrize("i", [-10, 0, 10])
def test_int_2(i):
    assert i % 1 == 0, 'Division reminder !=0 ==> i is not \'int\''


# негативный тест
# проверка, что число положительное
def test_int_3(i=-1):
    assert i < 0, 'number is positive'


# указанное число входит в указанное множество
def test_set_1(i=5):
    my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
    assert i in my_set, f'{i} not in test set'


# проверяем, что множество, созданное из списка с повторяющимися элементами будет короче этого списка
def test_set_2(test_list=[1, 1, 2, 2, 3, 3]):
    test_set = set(test_list)
    assert len(test_list) > len(test_set)


# проверяем, что при копировании множества сохраняется его тип
def test_set_3(test_set={'a, b, c'}):
    result_set = test_set.copy()
    assert isinstance(result_set, set)
