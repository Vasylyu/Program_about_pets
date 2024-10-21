class NamesAnimals:
    def __init__(self, name: str, command: str,
                 date_of_birth: str, kinds: str):
        self.name = name
        self.command = command
        self.date_of_birth = date_of_birth
        self.kinds = kinds

    def info(self, sep: str = ' '):
        return f'{self.name}{sep}{self.command}{sep}{self.date_of_birth}{sep}{self.kinds}'

    def field_len(self, field: str):
        if field == 'name':
            return len(self.name)
        elif field == 'command':
            return len(self.command)
        elif field == 'date_of_birth':
            return len(self.date_of_birth)
        elif field == 'kinds':
            return len(self.kinds)


class Zoo:
    def __init__(self, path: str = 'zoo.txt', separator: str = ':' ' '):
        self.zoo_list = {}
        self.path = path
        self.separator = separator

    def open_list_zoo(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            for a_id, animal in enumerate(file.readlines(), 1):
                animal = animal.strip().split(self.separator)
                self.zoo_list[a_id] = NamesAnimals(*animal)

    def save_list_zoo(self):
        data = []
        for animal in self.zoo_list.values():
            data.append(animal.info(self.separator))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def next_id_zoo(self):
        return (max(self.zoo_list) + 1) if self.zoo_list else 1

    def new_animal(self, animal: list[str]):
        self.zoo_list[self.next_id_zoo()] = NamesAnimals(*animal)

    def find_animal(self, word: str) -> 'Zoo':
        result = Zoo()
        for u_id, animal in self.zoo_list.items():
            if word.lower() in str(animal.info()).lower():
                result.zoo_list[u_id] = animal
        return result

    def change_commands(self, u_id: int, an_animal: list):
        self.zoo_list[u_id] = an_animal

    def max_len_zoo(self):
        max_field_lens = [0, 0, 0, 0]
        for animal in self.zoo_list.values():
            for n, field in enumerate(['name', 'command', 'date_of_birth', 'kinds']):
                if max_field_lens[n] < animal.field_len(field):
                    max_field_lens[n] = animal.field_len(field)
        return max_field_lens
