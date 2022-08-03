# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов


class Person:
    def __init__(self, population, name_room):
        self._population = population
        self._name_room = name_room

    def get_person_room(self):
        return self._name_room

    def get_city_population(self):
        return self._population


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

person = Person(231400, 34)
print(person.get_person_room())
print(person.get_city_population())
