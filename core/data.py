import unicodedata
import json

# Dictionary with rotors and reflector
rotor = {}
reflector = {}


def lecture_message(filename, result):
    with open(filename) as f:
        g = transform(f)
        result.append("".join(g))


def save_message(file_name, message_in):
    with open(file_name, mode="w") as f:
        f.write(message_in)


def load_params(settings_file):
    """ Setting the states of rotors """

    def init_rotor_and_reflector(rotors, reflecteurs):
        global rotor
        global reflector
        rotor = {str(k): str(rotors.get(k)) for k in rotors}
        reflector = {str(k): str(reflecteurs.get(k)) for k in reflecteurs}

    with open(settings_file, 'r') as p:
        init_rotor_and_reflector(**json.load(p))


def transform(message):
    for m in message:
        i = ("".join(
            d for d in unicodedata.normalize("NFD", str("".join(m.split())))
            if unicodedata.category(d) != "Mn"))
        if i:
            yield i.upper()
