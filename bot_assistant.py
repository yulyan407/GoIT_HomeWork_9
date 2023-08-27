import sys

CONTACTS_DICT = {}

def parse(user_input):
    """
    This function parse user input into command and arguments
    :param user_input: user input -> str
    :return: command -> str, args -> list
    """
    user_input_list = user_input.split(' ')
    command = user_input_list[0]
    args = user_input_list[1:]
    return (command, args)

def input_error(func):
    """
    This is a decorator function that catches errors that may occur when calling a function given as a parameter
    :param func -> function
    :return func if no error, str if there's an error
    """
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return 'The name is not in contacts. Enter user name please'
        except ValueError:
            return 'ValueError: Give me name and phone please'
        except IndexError:
            return 'IndexError: Give me name and phone please'
        except TypeError:
            return 'You entered invalid numbers of arguments for this command'
    return inner

@input_error
def add_contact(name, phone):
    """
    This function add the name with the phone in parameters into the CONTACTS_DICT
    :param name -> str
           phone -> str
    :return str
    """
    CONTACTS_DICT[name] = phone
    return f'Contact {name}: {phone} successfully added'

@input_error
def change_contact(name, phone):
    """
    This function change the phone for contact with the name that are given as parameters in the CONTACTS_DICT
    :param name -> str
           phone -> str
    :return str
    """
    CONTACTS_DICT.update({name: phone})
    return f'Contact {name}: {phone} successfully changed'

@input_error
def get_phone(name):
    """
    This function change the phone for contact with the name that are given as parameters in the CONTACTS_DICT
    :param name -> str
    :return phone -> str
    """
    phone = CONTACTS_DICT[name]
    return f'For {name} the phone is {phone}'

def show_all():
    """
    This function returns all contact from the CONTACTS_DICT
    :param: None
    :return: phone_book -> str
    """
    phone_book = ''
    for name, contact in CONTACTS_DICT.items():
        phone_book += f'{name} : {contact}\n'
    return phone_book

def greeting():
    return 'How can I help you?'

def end():
    return 'Good bye!'

def main():
    """
    This function implements all the logic of interaction with the user, all 'print' and 'input' takes place here
    :param: None
    :return: None
    """
    handler_commands = {'hello': greeting,
                        'hi': greeting,
                        'add': add_contact,
                        'change': change_contact,
                        'phone': get_phone,
                        'show all': show_all,
                        '.': end,
                        'good bye': end,
                        'close': end,
                        'exit': end}

    while True:
        user_input = input('>>>:')
        if user_input.lower() in handler_commands.keys():
            output = handler_commands[user_input.lower()]()
            print(output)
            if output == 'Good bye!':
                sys.exit()
        else:
            command, args = parse(user_input.lower())
            if command in handler_commands.keys():
                print(handler_commands[command](*args))
            else:
                print(
                    "You entered an invalid command, please enter one of the next commands: "
                    "'hello', 'hi', 'show all', 'add', 'change', 'phone', '.', 'good bye', 'close', 'exit'")


if __name__ == '__main__':
    main()