import sys

CONTACTS_DICT = {}


def parse(user_input):
    user_input_list = user_input.split(' ')
    command = user_input_list[0]
    args = user_input_list[1:]
    return (command, args)


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return 'The name is not in contacts. Enter user name again'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Give me name and phone please'

    return inner


@input_error
def add_contact(name, phone):
    CONTACTS_DICT[name] = phone
    return CONTACTS_DICT


@input_error
def change_contact(name, phone):
    CONTACTS_DICT.update({name: phone})
    return CONTACTS_DICT


@input_error
def get_phone(name):
    return CONTACTS_DICT[name]


def main():
    handler_commands = {'add': add_contact,
                        'change': change_contact,
                        'phone': get_phone}

    while True:
        user_input = input('>>>:')
        if user_input.lower() in ('.', 'good bye', 'close', 'exit'):
            print('Good bye!')
            sys.exit()
        elif user_input.lower() in ('hello', 'hi'):
            print('How can I help you?')
        elif user_input.lower() == 'show all':
            for name, contact in CONTACTS_DICT.items():
                print(f'{name}: {contact}')
        else:
            command, args = parse(user_input.lower())
            if command in handler_commands.keys():
                print(handler_commands[command](*args))
                # print(CONTACTS_DICT)
            else:
                print("You entered an invalid command, please enter one of the next commands:"
                    "'hello', 'hi', 'show all', 'add', 'change', 'phone',"
                      " '.', 'good bye', 'close', 'exit'")


if __name__ == '__main__':
    main()