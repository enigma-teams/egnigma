import unicodedata

import json

settings_file = "rotors.init"

message_file = "message.txt"

save_file = "sent.txt"

# Dictionary with rotors and reflector
rotor = {}
reflector = {}


def generate(it):
    for line in it:
        i = ("".join(
            d for d in unicodedata.normalize("NFD", unicode("".join(line.split()), encoding="utf-8"))
            if unicodedata.category(d) != "Mn"))
        if i:
            yield i.upper()


def lecture_message(filename, result):
    with open(filename) as f:
        g = generate(f)
        result.append("".join(g))


def save_message(file_name, message_to_send):
    with open(file_name, mode="w") as f:
        f.write(message_to_send)


def load_params():
    with open(settings_file, 'r') as p:
        init_rotor_and_reflector(**json.load(p))


def init_rotor_and_reflector(rotors, reflecteurs):
    """ Setting the states of rotors """
    global rotor
    global reflector
    rotor = rotors
    reflector = reflecteurs


def menu():
    message_to_sent = []
    lecture_message(message_file, message_to_sent)

    message = message_to_sent[0]

    load_params()

    print (reflector)

    mes = "Nouveau message"

    save_message(save_file, mes)
    print (message)


menu()
