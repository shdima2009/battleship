import random

class Field: #класс
    def __init__(self, size, ships): #параметры , метод
        self.size = size # атрибуты
        self.grid = [] # атрибуты
        for _ in range(size):
            self.grid.append([None] * size) #атрибут
        self.ships_alive = ships #атрибут

    def display(self, show_ships=False): # параметр, метод
        letters = "ABCDEFGHIJ" #переменная
        letter_string = "    " # переменная
        for letter in letters:
            letter_string += letter + " "

        print(letter_string)
        for i, row in enumerate(self.grid):
            display_row = ""
            for cell in row:
                if cell is None or (cell is not None and not show_ships):
                    display_row += "O "
                elif cell == 'X':
                    display_row += 'X '
                elif cell == '*':
                    display_row += '* '
                else:
                    display_row += "■ "
            if i + 1 != 10:
                print(i + 1, " ", display_row)
            else:
                print(i + 1, "", display_row)

class BattleshipGame: #класс
    def __init__(self): #метод
        self.size = 10 #атрибут
        self.ships = 15  #атрибут
        self.player_field = Field(self.size, self.ships) #обьект созданный внуттри init
        self.computer_field = Field(self.size, self.ships) #обьект созданный внуттри init


    def place_ships_randomly(self, field, num_ships): #метод
        for _ in range(num_ships):
            placed = False #переменная - флаг (поставлен ли корабль)
            while not placed:
                coords = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
                if self.is_valid_ship_placement(field, coords):
                    field.grid[coords[0]][coords[1]] = "S"
                    placed = True

    def is_valid_ship_placement(self, field, coords, ship_length=1, ): #метод
        x, y = coords

        for i in range(ship_length + 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    new_x, new_y = x + j, y + k
                    if 0 <= new_x < self.size and 0 <= new_y < self.size and field.grid[new_x][new_y] == "S":
                        return False

        return True

    def player_turn(self, x, y):
        x = "ABCDEFGHIJ".index(x)
        y -= 1

        if self.computer_field.grid[y][x] == "S":
            print('Вы попали!')
            self.computer_field.grid[y][x] = 'X'
            self.computer_field.ships_alive -= 1
        else:
            print('Вы не попали!')
            self.computer_field.grid[y][x] = '*'

    def computer_turn(self):
        x = random.randint(0, self.size-1)
        y = random.randint(0, self.size-1)

        if self.player_field.grid[y][x] == "S":
            print('Компьютер попал!')
            self.player_field.grid[y][x] = 'X'
            self.player_field.ships_alive -= 1
            # self.display_fields()
        elif self.player_field.grid[y][x] == '■':
            # self.display_fields()
            print('Вы уже стреляли в эту клетку!')
        else:
            print('Компьютер промахнулся!')
            self.player_field.grid[y][x] = '*'
            # self.display_fields()

    def display_fields(self):
        self.player_field.display(show_ships=True)
        self.computer_field.display(show_ships=True)


    def play(self): # метод
        print("Расстановка кораблей компьютера:")
        self.place_ships_randomly(self.computer_field, self.ships)
        self.computer_field.display(show_ships=True)
        print("Ваша расстановка кораблей:")
        self.place_ships_randomly(self.player_field, self.ships)
        self.player_field.display(show_ships=True)



        while True:
            x = input('Введите координату выстрела: ')
            y = int(input('Введите коородинату выстрела по y: '))
            self.player_turn(x, y)
            if self.computer_field.ships_alive == 0:
                print("Вы победили! Все корабли компьютера потоплены.")
                break


            self.computer_turn()

            if self.player_field.ships_alive == 0:
                print("Вы проиграли! Все ваши корабли потоплены.")
                break
            self.display_fields()


a = BattleshipGame() #обьект
a.play() #применяем метод к обьекту



