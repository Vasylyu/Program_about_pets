import text
from model import Zoo


def main_menu() -> int:
    for n, item in enumerate(text.main_menu):
        if n == 0:
            print(item)
        else:
            print(f'{n}. {item}')
    while True:
        choice = input(text.main_menu_choice)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return int(choice)
        print(f'Введите пункт меню от 1 до {len(text.main_menu) - 1}')


def show_animals(list_animal: Zoo, error_message: str):
    max_size = list_animal.max_len_zoo()
    if list_animal:
        print('\n' + '=' * (sum(max_size) + 7))
        for n, animal in list_animal.zoo_list.items():
            animal1 = 'собака'
            animal2 = 'кот'
            animal3 = 'хомяк'
            print(f'{n:>3}. {animal.name:<{max_size[0]}} '
                  f'{animal.command:<{max_size[1]}} '
                  f'{animal.date_of_birth:<{max_size[2]}} '
                  f'{animal.kinds:<{max_size[3]}}')
            if animal1 in animal.kinds:
                print(text.pets)
            elif animal2 in animal.kinds:
                print(text.pets)
            elif animal3 in animal.kinds:
                print(text.pets)
            else:
                print(text.pack_animals)
        print('=' * (sum(max_size) + 7) + '\n')
    else:
        print_message(error_message)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def add_animal(message: list[str], animal: list[str] = None):
    animal = animal if animal else ['', '', '', '']
    for n, mes in enumerate(message):
        field = input(mes)
        animal = list(animal)
        animal[n] = field if field else (animal[n])
    return animal


def input_data(message: str) -> str:
    return input(message)
