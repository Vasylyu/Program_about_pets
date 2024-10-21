import view
import model
import text


def find_animal(animals: model.Zoo):
    word = view.input_data(text.input_search_word)
    result = animals.find_animal(word)
    view.show_animals(result, text.animals_not_found(word))


def start_app():
    na = model.Zoo()
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                na.open_list_zoo()
                view.print_message(text.load_successful)
            case 2:
                na.save_list_zoo()
                view.print_message(text.save_successful)
            case 3:
                view.show_animals(na, text.empty_list_zoo)
            case 4:
                animal = view.add_animal(text.new_animal)
                na.new_animal(animal)
                view.print_message(text.new_animal_added_successful(animal[0]))
            case 5:
                find_animal(na)
            case 6:
                find_animal(na)
                while True:
                    try:
                        u_id = int(view.input_data(text.input_id_change_animal))
                        if u_id == str:
                            raise ValueError(str)
                        if u_id == int:
                            return int(u_id)
                        break
                    except ValueError:
                        print('ValueError!')
                        print('Введите целое число!')
                        continue
                    finally:
                        pass
                an_animal = view.add_animal(text.learn_animal, na.zoo_list)
                na.change_commands(u_id, an_animal)
                view.print_message(text.animal_learn_successful(an_animal[1]))

            case 7:
                view.print_message(text.see_you_late)

                break
