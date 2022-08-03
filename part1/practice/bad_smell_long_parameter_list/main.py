# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, field, x_coord: int, y_coord: int, state: str, speed: int = 1):
        self._field = field
        self._x = x_coord
        self._y = y_coord
        self._state = state.lower()
        self._speed = speed

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self._field.set_unit(x=self._x, y=self._y + speed, unit=self)
        elif direction == 'DOWN':
            self._field.set_unit(x=self._x, y=self._y - speed, unit=self)
        elif direction == 'LEFT':
            self._field.set_unit(x=self._x - speed, y=self._y, unit=self)
        elif direction == 'RIGHT':
            self._field.set_unit(x=self._x + speed, y=self._y, unit=self)

    def _get_speed(self):
        if self._state == 'fly':
            return self._speed * 1.2
        elif self._state == 'crawl':
            return self._speed * 0.5
        else:
            raise ValueError('А вот сейчас не понял')
