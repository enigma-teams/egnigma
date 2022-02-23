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


def encrypt(letter, key, selector_direction):
    global rotor
    for name in list(rotor.keys())[::selector_direction]:
        letter_index = list(rotor.get(name)).index(letter)
        if letter_index + key <= len(rotor.get(name)) - 1:
            letter = rotor.get(name)[letter_index + key]
        else:
            letter = rotor.get(name)[letter_index + key - len(rotor.get(name))]
        rotor_permute(name, key)
    return letter


def rotor_permute(rotor_name, key):
    global rotor
    rotor_value = list(rotor.get(rotor_name))
    for i in range(key):
        rotor_value.insert(0, rotor_value[-1])
        rotor_value.pop(-1)

    rotor.update({rotor_name: "".join(rotor_value)})


def init_rotor_and_reflector(rotors, reflecteurs):
    """ Setting the states of rotors """
    global rotor
    global reflector
    rotor = {key: rotors.get(key) for key in sorted(rotors)}
    reflector = {key: rotors.get(key) for key in sorted(reflecteurs)}


def menu():
    message_to_sent = []
    lecture_message(message_file, message_to_sent)

    message = message_to_sent[0]

    load_params()

    save_message(save_file, "".join(encrypt(str(m), 3, 1) for m in message))
    print (message)


menu()
