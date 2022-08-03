# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def move(self, field, x_pos: int, y_pos: int, direction, is_fly: bool, crawl: bool, speed: int = 1):

        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            new_x, new_y = self._calculation_new_pos(direction, x_pos, y_pos, speed)

        if crawl:
            speed *= 0.5
            new_x, new_y = self._calculation_new_pos(direction, x_pos, y_pos, speed)

        field.set_unit(x=new_x, y=new_y, unit=self)

    @staticmethod
    def _calculation_new_pos(direction, x_pos: int, y_pos: int, speed: int) -> tuple:
        if direction == 'UP':
            new_y = y_pos + speed
            new_x = x_pos
        elif direction == 'DOWN':
            new_y = y_pos - speed
            new_x = x_pos
        elif direction == 'LEFT':
            new_y = y_pos
            new_x = x_pos - speed
        elif direction == 'RIGHT':
            new_y = y_pos
            new_x = x_pos + speed

        return (new_x, new_y)
