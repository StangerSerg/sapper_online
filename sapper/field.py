from random import randint


class Cell:
    fl_open = False
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine


class GamePole:
    def __init__(self, field_size, mines_count):
        self.field_size = field_size
        self.mines_count = mines_count
        self.pole = [[Cell(0, False) for i in range(field_size)] for j in range(field_size)]
        self.create()


    def create(self):
        '''
        Функция заполнения полей минами и числами, обозначающими
        количество мин вокруг поля.
        '''
        if self.mines_count > self.field_size ** 2:
            print('Количество мин превышает количество клеток')
            return False
        i = 0
        while i < self.mines_count:
            row_num, col_num = randint(0, self.field_size-1), randint(0, self.field_size-1)
            if not self.pole[row_num][col_num].mine:
                self.pole[row_num][col_num].mine = True
                self.set_around_mines(row_num, col_num)
                self.pole[row_num][col_num].around_mines = 0
                i += 1

    def set_around_mines(self, row_num, col_num):
        '''
        Вспомогательная функция заполнения полей числами, обозначающими
        количество мин вокруг поля.
        '''
        cells = []
        row_from = row_num - 1 if row_num > 0 else 0
        row_to = row_num + 2 if row_num + 2 < self.field_size else self.field_size
        col_from = col_num - 1 if col_num > 0 else 0
        col_to = col_num + 2 if col_num + 2 < self.field_size else self.field_size
        for row in self.pole[row_from:row_to]:
            cells += row[col_from:col_to]
        for cell in cells:
            cell.around_mines += 1



    def show(self):
        res = [['#' if not cell.fl_open else '*' if cell.mine else cell.around_mines for cell in row] for row in self.pole]
        for row in res:
            print(*row)


new_field = GamePole(10, 12)

new_field.show()


